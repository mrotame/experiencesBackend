from django.test import TestCase
from ..models.users import Users
from .setupTest import SetupTest

class TestUsersViewPatch(SetupTest, TestCase):

    def test_realiza_alteracao_sem_credencial_e_retorna_erro(self):
        url = self.url + f'{self.usuarioComum.id}/'
        res = self.app.patch(url)
        self.assertEqual(res.status_code, 401)

    def test_realiza_alteracao_sem_credencial_e_sem_id_e_retorna_erro_400(self):
        res = self.app.patch(self.url)
        self.assertEqual(res.status_code, 400)

    def test_realiza_alteracao_sem_id_com_credencial_comum_e_retorna_erro_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        res = self.app.patch(self.url, **headers)

        self.assertEqual(res.status_code, 403)

    def test_realiza_alteracao_com_credencial_comum_com_id_de_outro_usuario_e_retorna_403(self):
        url = self.url + f'{self.usuarioComum2.id}/'

        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        res = self.app.patch(url, **headers)
        self.assertEqual(res.status_code, 403)

    def test_realiza_alteracao_com_credencial_comum_com_proprio_id_e_retorna_200(self):
        url = self.url + f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Teste Teste"}
        res = self.app.patch(url, data, **headers)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_comum_com_proprio_id_e_verifica_alteracao_no_banco(self):
        url = self.url + f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Teste Teste"}
        res = self.app.patch(url, data, **headers)

        query = Users.objects.filter(nome="Teste Teste Teste")
        self.assertEqual(query.count(), 1)

    def test_realiza_alteracao_com_credencial_admin_com_proprio_id_e_retorna_200(self):
        url = self.url + f'{self.usuarioAdmin.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Admin Admin Admin"}
        res = self.app.patch(url, data, **headers)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_admin_com_proprio_id_e_verifica_alteracao_no_banco(self):
        url = self.url + f'{self.usuarioAdmin.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Admin Admin Admin"}
        res = self.app.patch(url, data, **headers)

        query = Users.objects.filter(nome="Admin Admin Admin")
        self.assertEqual(query.count(), 1)

    def test_realiza_alteracao_com_credencial_admin_com_outro_id_e_retorna_200(self):
        url = self.url + f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Admin Teste Admin Teste Admin"}
        res = self.app.patch(url, data, **headers)
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_valida_com_credencial_admin_com_id_de_outro_usuario_e_verifica_alteracao_no_banco(self):
        url = self.url + f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {'HTTP_AUTHORIZATION':f'Bearer {token}'}
        data = {"nome":"Teste Admin Teste Admin Teste Admin"}
        res = self.app.patch(url, data, **headers)

        query = Users.objects.filter(nome="Teste Admin Teste Admin Teste Admin")
        self.assertEqual(query.count(), 1)