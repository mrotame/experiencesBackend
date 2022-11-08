from django.test import TestCase
from ..listaExperiencias import ListaExperiencias
from experiencias.models import Experiencias
from .setupTest import SetupTest

class UpdateAllView(SetupTest, TestCase):
    def setUp(self, criaUsuarios=True, criaExperiencias=False) -> None:
        return super().setUp(criaUsuarios, criaExperiencias)

    def afterSetUp(self) -> None:
        self.url += 'updateall/'
        return super().afterSetUp()

    def test_realiza_request_como_usuario_comum_e_retorna_403(self):
        token = self.get_tokens_for_user(self.usuarioComum)['access']
        headers = {"HTTP_AUTHORIZATION":f"Bearer {token}"}
        res = self.app.post(self.url, **headers)
        # breakpoint()
        self.assertEqual(res.status_code, 403)

    def test_realiza_request_como_usuario_admin_e_retorna_200(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']
        headers = {"HTTP_AUTHORIZATION":f"Bearer {token}"}
        res = self.app.post(self.url, **headers)
        # breakpoint()
        self.assertEqual(res.status_code, 200)

    def test_realiza_request_e_verifica_se_todas_as_experiencias_foram_setadas_no_banco(self):
        token = self.get_tokens_for_user(self.usuarioAdmin)['access']
        headers = {"HTTP_AUTHORIZATION":f"Bearer {token}"}
        res = self.app.post(self.url, **headers)
        query = Experiencias.objects.all()
        self.assertEqual(query.count(),len(ListaExperiencias().todas))