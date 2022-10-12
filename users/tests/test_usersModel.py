from django.test import TestCase
from ..models.users import Users
from django.core.exceptions import ValidationError

class TestUsersModel(TestCase):

    def test_cria_usuario_correto_e_valida_usuario_criado_no_banco(self):
        Users.objects.create(
            nome="teste_correto",
            email="teste@teste.com",
            is_staff=0,
            is_active=1,
            is_superuser = 0,
            password="123"
        )

        self.assertEquals(Users.objects.count(), 1)

    def test_cria_usuario_sem_nome_e_valida_usuario_criado_no_banco(self):
        Users.objects.create(
            email="teste_sem_nome@teste.com",
            is_staff=0,
            is_active=1,
            is_superuser = 0,
            password="123"
        )

        self.assertEquals(Users.objects.filter(email="teste_sem_nome@teste.com").count(), 1)

    def test_cria_usuario_sem_email_e_retorna_erro(self):
        def createUser():
            Users.objects.create(
                nome="teste_sem_email",
                is_staff=0,
                is_active=1,
                is_superuser = 0,
                password="123"
            )
            breakpoint()
        self.assertRaises(ValidationError, createUser)
