from datetime import datetime
from django.test import TestCase
from ..models import Experiencias
from .setupTest import SetupTest

class TestUsersViewDelete(SetupTest, TestCase):

    def test_realiza_request_sem_credencial_e_retorna_erro_401(self):
        url = self.url + f'{self.experiencia.id}/'
        res = self.app.delete(url)

        self.assertEqual(res.status_code, 401)

    def test_realiza_alteracao_sem_credencial_e_sem_id_e_retorna_erro_401(self):
        res = self.app.delete(self.url)
        self.assertEqual(res.status_code, 401)

    def test_realiza_alteracao_com_credencial_comum_e_sem_id_e_retorna_erro_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(self.url, **headers)
        self.assertEqual(res.status_code, 403)

    def test_realiza_alteracao_com_credencial_admin_e_sem_id_e_retorna_erro_403(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(self.url, **headers)
        self.assertEqual(res.status_code, 400)

    def test_realiza_request_com_credencial_comum_e_retorna_erro(self):
        url = self.url + f'{self.experiencia2.id}/'
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(url, **headers)

        self.assertEqual(res.status_code, 403)

    def test_realiza_request_com_credencial_admin_e_verifica_se_experiencia_ainda_esta_no_banco(self):
        url = self.url + f'{self.experiencia.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(url, **headers)

        experiencia_deletada_raw = None
        for p in Experiencias.objects.raw('select * from experiencias_experiencias'): 
            if p.nome == self.experiencia.nome:
                experiencia_deletada_raw = p

        self.assertNotEqual(experiencia_deletada_raw, None)

    def test_realiza_request_com_credencial_admin_e_verifica_que_experiencia_nao_esta_mais_na_lista_de_experiencias(self):
        url = self.url + f'{self.experiencia.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(url, **headers)

        lista_nomes_experiencias = [experiencia.nome for experiencia in Experiencias.objects.all()]
        self.assertNotIn(self.experiencia.nome, lista_nomes_experiencias)

    def test_realiza_request_com_credencial_admin_e_verifica_que_experiencia_esta_com_campo_deleted_at_preenchido(self):
        url = self.url + f'{self.experiencia.id}/'

        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
        res = self.app.delete(url, **headers)

        self.experiencia.refresh_from_db()
        self.assertEqual(type(self.experiencia.deleted_at),datetime)

    # def test_realiza_request_com_credencial_admin_com_proprio_id_e_retorna_200(self):
    #     url = self.url + f'{self.usuarioAdmin.id}/'
    #     token = self.get_tokens_for_user(self.usuarioAdmin)['access']

    #     headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
    #     res = self.app.delete(url, **headers)

    #     self.assertEqual(res.status_code, 204)

    # def test_realiza_request_com_credencial_admin_com_outro_id_e_retorna_200(self):
    #     url = self.url + f'{self.experiencia.id}/'
    #     token = self.get_tokens_for_user(self.usuarioAdmin)['access']

    #     headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
    #     res = self.app.delete(url, **headers)

    #     self.assertEqual(res.status_code, 204)

    # def test_realiza_request_com_credencial_admin_com_proprio_id_e_verifica_que_usuario_esta_fora_da_lista_de_usuarios(self):
    #     url = self.url + f'{self.usuarioAdmin.id}/'

    #     token = self.get_tokens_for_user(self.usuarioAdmin)['access']

    #     headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
    #     res = self.app.delete(url, **headers)

    #     lista_nomes_experiencias = [experiencia.nome for experiencia in Experiencias.objects.all()]
    #     self.assertNotIn(self.usuarioAdmin.email, lista_nomes_experiencias)

    # def test_realiza_request_com_credencial_admin_deletada_com_id_de_outro_usuario_e_retorna_401(self):
    #     url_usuarioAdmin = self.url + f'{self.usuarioAdmin.id}/'
    #     url_experiencia = self.url + f'{self.experiencia.id}/'
    #     token = self.get_tokens_for_user(self.usuarioAdmin)['access']

    #     headers = {"HTTP_AUTHORIZATION":f'Bearer {token}'}
    #     self.app.delete(url_usuarioAdmin, **headers)
    #     res = self.app.delete(url_experiencia, **headers)

    #     self.assertEqual(res.status_code, 401)