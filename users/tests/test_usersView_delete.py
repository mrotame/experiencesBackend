from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..views.users import UsersGenericView
from ..models.users import Users
from .setupTest import SetupTest

class TestUsersViewDelete(SetupTest, TestCase):

    def test_realiza_request_sem_credencial_e_retorna_erro(self):
        req = self.app.delete(self.url)
        res = self.view(req, id=self.usuarioComum.id)

        self.assertEqual(res.status_code, 401)

    def test_realiza_alteracao_sem_credencial_e_sem_id_e_retorna_erro_400(self):
        req = self.app.delete(self.url)
        res = self.view(req)
        self.assertEqual(res.status_code, 400)

    def test_realiza_request_com_credencial_comum_com_id_de_outro_usuario_e_retorna_erro(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":token}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum2.id)

        self.assertEqual(res.status_code, 401)

    def test_realiza_request_com_credencial_comum_com_proprio_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        self.assertEqual(res.status_code, 204)

    def test_realiza_request_com_credencial_comum_com_proprio_id_verifica_que_usuario_ainda_esta_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        deleted_user_raw = None
        for p in Users.objects.raw('select * from users_users'): 
            if p.email == self.usuarioComum.email:
                deleted_user_raw = p

        self.assertNotEqual(deleted_user_raw, None)

    def test_realiza_request_com_credencial_comum_com_proprio_id_verifica_que_usuario_nao_esta_mais_na_lista_de_usuarios(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        lista_emails_usuarios = [usuario.email for usuario in Users.objects.all()]
        self.assertNotIn(self.usuarioComum.email, lista_emails_usuarios)

    def test_realiza_request_com_credencial_comum_com_proprio_id_verifica_que_usuario_esta_com_campo_deleted_at_preenchido(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        self.usuarioComum.refresh_from_db()
        self.assertEqual(type(self.usuarioComum.deleted_at),datetime)

    def test_realiza_request_com_credencial_admin_com_proprio_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioAdmin.id)

        self.assertEqual(res.status_code, 204)

    def test_realiza_request_com_credencial_admin_com_outro_id_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        self.assertEqual(res.status_code, 204)

    def test_realiza_request_com_credencial_admin_com_proprio_id_e_verifica_que_usuario_esta_fora_da_lista_de_usuarios(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        res = self.view(req, id=self.usuarioComum.id)

        lista_emails_usuarios = [usuario.email for usuario in Users.objects.all()]
        self.assertNotIn(self.usuarioComum.email, lista_emails_usuarios)

    def test_realiza_request_com_credencial_admin_deletada_com_id_de_outro_usuario_e_retorna_401(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        req = self.app.delete(self.url, **headers)
        self.view(req, id=self.usuarioAdmin.id)

        res = self.view(req, id=self.usuarioAdmin.id)
        self.assertEqual(res.status_code, 401)