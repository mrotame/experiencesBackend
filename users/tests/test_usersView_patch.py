from django.test import TestCase
from ..models.users import Users
from ..views.users import UsersGenericView
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken

class TestUsersViewPatch(TestCase):
    url = '/usuarios'

    def criaUsuario(self, email:str, password="12345", admin:bool=False)->Users:
        user = Users.objects.create(
            email=email,
            is_active=True,
            is_superuser=admin,
            is_staff=admin
        )
        user.set_password(password)
        return user

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def setUp(self):
        self.app = APIRequestFactory()
        self.view = UsersGenericView.as_view()
        
        self.usuarioComum = self.criaUsuario("teste@teste.com")
        self.usuarioComum2 = self.criaUsuario("teste2@teste.com")

        self.usuarioAdmin = self.criaUsuario("testeadmin@teste.com", admin=True)

    def test_realiza_alteracao_sem_credencial_e_retorna_erro(self):
        req = self.app.patch(self.url)
        res = self.view(req, id=self.usuarioComum.id)
        self.assertEqual(res.status_code, 401)

    def test_realiza_alteracao_sem_credencial_e_sem_id_e_retorna_erro_400(self):
        req = self.app.patch(self.url)
        res = self.view(req)
        self.assertEqual(res.status_code, 400)

    def test_realiza_alteracao_sem_id_com_credencial_comum_e_retorna_erro_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        req = self.app.patch(self.url, **headers)
        res = self.view(req)

        self.assertEqual(res.status_code, 403)

    def test_realiza_alteracao_com_credencial_comum_com_id_de_outro_usuario_e_retorna_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        req = self.app.patch(self.url, **headers)
        res = self.view(req, id=self.usuarioComum2.id)
        self.assertEqual(res.status_code, 403)

    def test_realiza_alteracao_com_credencial_comum_com_proprio_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Teste Teste"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioComum.id)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_comum_e_verifica_alteracao_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Teste Teste"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        query = Users.objects.filter(nome="Teste Teste Teste")
        self.assertEqual(query.count(), 1)

    def test_realiza_alteracao_com_credencial_admin_com_proprio_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Admin Admin Admin"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioAdmin.id)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_admin_com_proprio_id_e_verifica_alteracao_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Admin Admin Admin"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioAdmin.id)

        query = Users.objects.filter(nome="Admin Admin Admin")
        self.assertEqual(query.count(), 1)

    def test_realiza_alteracao_com_credencial_admin_com_outro_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Admin Teste Admin Teste Admin"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioComum.id)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_admin_com_id_de_outro_usuario_e_verifica_alteracao_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Admin Teste Admin Teste Admin"}
        req = self.app.patch(self.url, data, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        query = Users.objects.filter(nome="Teste Admin Teste Admin Teste Admin")
        self.assertEqual(query.count(), 1)