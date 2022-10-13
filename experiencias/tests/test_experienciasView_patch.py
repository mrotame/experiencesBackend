from .setupTest import SetupTest
from django.test import TestCase
from ..models import Experiencias

class TestExperienciasViewPost(SetupTest, TestCase):
    def test_realiza_request_para_alterar_nome_da_experiencia_como_admin_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']
        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        url = self.url + f'{self.experiencia.id}/'

        res = self.app.patch(url, {"nome":"Patch Testing"}, **headers)

        self.assertEqual(res.status_code, 200)

    def test_realiza_request_para_alterar_nome_da_experiencia_como_admin_e_verifica_resultado_alterado_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']
        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        url = self.url + f'{self.experiencia.id}/'

        res = self.app.patch(url, {"nome":"Patch Testing"}, **headers)
        query = Experiencias.objects.filter(nome="Patch Testing")

        self.assertEqual(query.count(), 1)

    def test_realiza_request_para_alterar_nome_da_experiencia_como_admin_sem_id_e_retorna_404(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']
        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}

        res = self.app.patch(self.url, {"nome":"Patch Testing"}, **headers)

        self.assertEqual(res.status_code, 400)

    def test_realiza_request_para_alterar_nome_da_experiencia_como_usuario_comum_e_retorna_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']
        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}

        res = self.app.patch(self.url, {"nome":"Patch Testing"}, **headers)
        self.assertEqual(res.status_code, 403)

    def test_realiza_request_para_alterar_nome_da_experiencia_sem_credencial_e_retorna_401(self):
        res = self.app.patch(self.url, {"nome":"Patch Testing"})
        self.assertEqual(res.status_code, 401)

    def test_realiza_request_para_alterar_nome_da_experiencia_com_credencial_incorreta_e_retorna_403(self):
        headers = {"HTTP_AUTHORIZATION": b'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'}

        res = self.app.patch(self.url, {"nome":"Patch Testing"}, **headers)
        self.assertEqual(res.status_code, 401)

    def test_realiza_request_para_alterar_nome_da_experiencia_com_credencial_invalida_e_retorna_403(self):
        headers = {"HTTP_AUTHORIZATION": b'Bearer 123456789'}

        res = self.app.patch(self.url, {"nome":"Patch Testing"}, **headers)
        self.assertEqual(res.status_code, 401)