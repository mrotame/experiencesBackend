from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from ..models.users import Users
from ..views.users import UsersGenericView

class TestUsersViewGet(TestCase):
    url = "/usuarios"

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

        self.usuarioComum = self.criaUsuario("teste@teste.com")
        self.usuarioComum2 = self.criaUsuario("teste2@teste.com")

        self.usuarioAdmin = self.criaUsuario("testeadmin@teste.com", admin=True)

    def test_realiza_request_get_sem_credencial_e_retorna_401(self):
        req = self.app.get(self.url)
        res = UsersGenericView.as_view()(req)
        self.assertEquals(res.status_code, 401)

    def test_realiza_request_get_com_credencial_invalida_401(self):
        headers={'HTTP_AUTHORIZATION':"Bearer 123456"}
        req = self.app.get(self.url, **headers)
        res = UsersGenericView.as_view()(req)
        self.assertEquals(res.status_code, 401)
    
    def test_realiza_request_get_com_credencial_de_superuser_e_retorna_200(self):

        token = self.get_tokens_for_user(self.usuarioAdmin)
        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(self.url, **headers)
        res = UsersGenericView.as_view()(req)
        
        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_credencial_de_usuario_comum_e_retorna_301(self):

        token = self.get_tokens_for_user(self.usuarioComum)
        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(self.url, **headers)
        res = UsersGenericView.as_view()(req)
        self.assertEquals(res.status_code, 403)

    def test_realiza_request_get_com_id_sem_credencial_e_retorna_401(self):
        url = self.url + '/1'
        req = self.app.get(url)
        res = UsersGenericView.as_view()(req)
        self.assertEquals(res.status_code, 401)

    def test_realiza_request_get_com_id_de_outro_usuario_com_credencial_comum_e_retorna_403(self):
        url = self.url + f'/{self.usuarioComum2.id}'
        token = self.get_tokens_for_user(self.usuarioComum)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(url, **headers)
        res = UsersGenericView.as_view()(req)
        self.assertEquals(res.status_code, 403)

    def test_realiza_request_get_com_proprio_id_com_credencial_comum_e_retorna_200(self):
        user = self.usuarioComum
        token = self.get_tokens_for_user(user)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(self.url,**headers)
        res = UsersGenericView.as_view()(req, id=user.id)

        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_proprio_id_com_credencial_admin_e_retorna_200(self):
        user = self.usuarioAdmin
        token = self.get_tokens_for_user(user)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(self.url, **headers)
        res = UsersGenericView.as_view()(req, id=user.id)

        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_outro_id_com_credencial_admin_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        req = self.app.get(self.url, **headers)
        res = UsersGenericView.as_view()(req, id=self.usuarioComum.id)

        self.assertEquals(res.status_code, 200)
    

    