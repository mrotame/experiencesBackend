from django.test import TestCase
from main.tests import DefaultTestCase


class SetupTest(DefaultTestCase, TestCase):
    url: str

    def setUp(self) -> None:
        self.url = self.usersView[1]
        self.view = self.usersView[0]

        self.usuarioComum = self.criaUsuario("teste@teste.com")
        self.usuarioComum2 = self.criaUsuario("teste2@teste.com")
        self.usuarioAdmin = self.criaUsuario("testeadmin@teste.com", admin=True)

        return super().setUp()