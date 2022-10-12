from main.tests import DefaultTestCase
from django.test import TestCase

class SetupTest(DefaultTestCase, TestCase):
    url: str
    def setUp(self) -> None:
        self.view = self.experienciasView[0]
        self.url = self.experienciasView[1]

        self.experiencia = self.criaExperiencia("teste1")
        self.experiencia2 = self.criaExperiencia("teste2")
        self.usuarioComum = self.criaUsuario("teste@teste.com")
        self.usuarioAdmin = self.criaUsuario("testeAdmin@teste.com", admin=True)
        return super().setUp()