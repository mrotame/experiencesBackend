from django.test import TestCase
from .setupTest import SetupTest
from ..models import Experiencias

class TestExperienciasViewGet(SetupTest, TestCase):
    def test_realiza_busca_sem_id_e_retorna_200(self):
        res = self.app.get(self.url)

        self.assertEqual(res.status_code, 200)

    def test_realiza_busca_sem_id_e_verifica_se_tamanho_retornado_corresponde_ao_tamanho_do_banco(self):
        res = self.app.get(self.url)

        self.assertEqual(len(res.data), Experiencias.objects.all().count())

    def test_realiza_busca_com_id_e_retorna_200(self):
        url = self.url + f'{self.experiencia.id}/'
        res = self.app.get(url)

        self.assertEqual(res.status_code,200)

    def test_realiza_busca_com_credencial_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']
        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.get(self.url, **headers)
        self.assertEqual(res.status_code,200)