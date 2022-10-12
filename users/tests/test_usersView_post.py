from django.test import TestCase
from ..models.users import Users
from .setupTest import SetupTest

class TestUsersViewPost(SetupTest, TestCase):

    def test_cadastra_novo_usuario_e_retorna_201(self):
        data = {'email':"teste_post@teste.com","password":"12345", 'nome':'teste'}
        res = self.app.post(self.url, data)
        self.assertEqual(res.status_code, 201)

    def test_cadastra_novo_usuario_e_verifica_email_do_usuario_criado_no_banco(self):

        data = {'email':"teste_post@teste.com","password":"12345", 'nome':'teste'}
        res = self.app.post(self.url, data)
        user = Users.objects.filter(email="teste_post@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.count(), 1)

    def test_cadastra_novo_usuario_e_verifica_se_senha_esta_criptografada(self):
        data = {'email':"teste_post@teste.com","password":"12345", 'nome':'teste'}

        res = self.app.post(self.url, data)
        user = Users.objects.get(email="teste_post@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertTrue("pbkdf2" in user.password)

    def test_cadastra_novo_usuario_e_verifica_que_usuario_nao_e_superuser(self):
        data = {'email':"teste_post@teste.com","password":"12345", 'nome':'teste'}

        res = self.app.post(self.url, data)
        user = Users.objects.get(email="teste_post@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.is_superuser, False)

    def test_cadastra_novo_usuario_e_verifica_que_usuario_nao_esta_ativo(self):
        data = {'email':"teste_post@teste.com","password":"12345", 'nome':'teste'}

        res = self.app.post(self.url, data)
        user = Users.objects.get(email="teste_post@teste.com")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.is_active, False)

    def test_cadastra_novo_usuario_sem_email_e_retorna_erro(self):
        data = {"password":"12345", 'nome':'teste'}

        res = self.app.post(self.url, data)
        self.assertEqual(res.status_code, 400)

    def test_cadastra_novo_usuario_sem_senha_e_retorna_erro(self):
        data = {'email':"teste_post@teste.com", 'nome':'teste'}

        res = self.app.post(self.url, data)
        self.assertEqual(res.status_code, 400)

    def test_cadastra_novo_usuario_sem_nome_e_retorna_erro(self):
        data = {'email':"teste_post@teste.com", "password":"12345"}

        res = self.app.post(self.url, data)
        self.assertEqual(res.status_code, 400)

    def test_cadastra_novo_usuario_com_email_invalido_e_retorna_erro(self):
        data = {'email':"testetesteteste", "nome":"teste","password":"12345"}

        res = self.app.post(self.url, data)
        self.assertEqual(res.status_code, 400)

    