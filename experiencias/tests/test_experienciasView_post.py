from .setupTest import SetupTest
from django.test import TestCase
from ..models import Experiencias

class TestExperienciasViewPost(SetupTest, TestCase):
    def setUp(self) -> None:
        self.post_data = {"nome":"teste", "subnome":"post", "desc":"teste","data_inicio":"01/01/2022", "data_fim": "12/10/2022","tags":"Teste Teste Teste"}
        return super().setUp()

    def test_realiza_criacao_sem_credencial_e_sem_json_e_retorna_401(self):
        res = self.app.post(self.url)

        self.assertEqual(res.status_code,401)

    def test_realiza_criacao_sem_credencial_com_json_e_retorna_401(self):
        
        res = self.app.post(self.url, self.post_data)

        self.assertEqual(res.status_code,401)
        
    def test_realiza_criacao_com_credencial_comum_e_retorna_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code,403)

    def test_realiza_criacao_com_credencial_admin_sem_json_e_retorna_401(self):

        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, **headers)

        self.assertEqual(res.status_code, 400)

    def test_realiza_criacao_com_credencial_admin_com_json_sem_nome_e_retorna_400(self):
        del self.post_data["nome"]
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code, 400)

    def test_realiza_criacao_com_credencial_admin_com_json_sem_desc_e_retorna_400(self):
        del self.post_data["desc"]
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code, 400)

    def test_realiza_criacao_com_credencial_admin_com_json_sem_data_inicio_e_retorna_400(self):
        del self.post_data["data_inicio"]
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code, 400)
    
    def test_realiza_criacao_com_credencial_admin_com_json_e_retorna_201(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code, 201)

    def test_realiza_criacao_com_credencial_admin_com_json_sem_data_fim_e_retorna_201(self):
        del self.post_data["data_fim"]
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        self.assertEqual(res.status_code, 201)

    def test_realiza_criacao_com_credencial_admin_com_json_e_verifica_experiencia_no_banco(self):
        self.post_data['nome'] = "post test database"
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']

        headers = {"HTTP_AUTHORIZATION": f'Bearer {token}'}
        res = self.app.post(self.url, self.post_data, **headers)

        query = Experiencias.objects.filter(nome=self.post_data['nome'])

        self.assertEqual(query.count(), 1)