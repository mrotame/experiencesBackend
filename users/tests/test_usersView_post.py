from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..views.users import UsersGenericView
from ..models.users import Users

class TestUsersViewPost(TestCase):
    url: str = '/usuarios'

    def setUp(self):
        self.app = APIRequestFactory()

    def test_cadastra_novo_usuario_e_retorna_201(self):
        data = {'email':"teste@teste.com","password":"12345", 'nome':'teste'}
        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        self.assertEqual(res.status_code, 201)

    def test_cadastra_novo_usuario_e_verifica_email_do_usuario_criado_no_banco(self):

        data = {'email':"teste@teste.com","password":"12345", 'nome':'teste'}
        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        user = Users.objects.filter(email="teste@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.count(), 1)

    def test_cadastra_novo_usuario_e_verifica_se_senha_esta_criptografada(self):
        data = {'email':"teste@teste.com","password":"12345", 'nome':'teste'}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        user = Users.objects.get(email="teste@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertTrue("pbkdf2" in user.password)

    def test_cadastra_novo_usuario_e_verifica_que_usuario_nao_e_superuser(self):
        data = {'email':"teste@teste.com","password":"12345", 'nome':'teste'}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        user = Users.objects.get(email="teste@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.is_superuser, False)

    def test_cadastra_novo_usuario_e_verifica_que_usuario_nao_esta_ativo(self):
        data = {'email':"teste@teste.com","password":"12345", 'nome':'teste'}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        user = Users.objects.get(email="teste@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.is_active, False)

    def test_cadastra_novo_usuario_sem_email_e_retorna_erro(self):
        data = {"password":"12345", 'nome':'teste'}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        self.assertEqual(res.status_code, 400)

    def test_cadastra_novo_usuario_sem_senha_e_retorna_erro(self):
        data = {'email':"teste@teste.com", 'nome':'teste'}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        self.assertEqual(res.status_code, 400)

    def test_cadastra_novo_usuario_sem_nome_e_retorna_erro(self):
        data = {'email':"teste@teste.com", "password":"12345"}

        req = self.app.post(self.url, data)
        res = UsersGenericView.as_view()(req)
        self.assertEqual(res.status_code, 400)

    