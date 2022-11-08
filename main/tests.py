from typing import Dict
from django.test import TestCase
from experiencias.models import Experiencias
from users.models.users import Users
from rest_framework_simplejwt.tokens import RefreshToken
from users.views.users import UsersGenericView
from experiencias.views.experienciasView import ExperienciasGenericView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.test import APIClient
from datetime import datetime, timedelta
import logging

class DefaultTestCase(TestCase):
    usersView = (UsersGenericView.as_view(), '/usuarios/')
    experienciasView = (ExperienciasGenericView.as_view(), '/experiencias/')
    sessionTokenView = (TokenObtainPairView.as_view(), '/token/')
    sessionRefreshView = (TokenRefreshView.as_view(), '/refresh/')
    app = APIClient()

    def setUp(self) -> None:
        logger = logging.getLogger('django.request')
        previous_level = logger.getEffectiveLevel()
        logger.setLevel(logging.ERROR)
        self.afterSetUp()
        return super().setUp()

    def afterSetUp(self, *args, **kwargs):
        pass


    def criaUsuario(self, email:str, password="12345", admin:bool=False)->Users:
        user = Users.objects.create(
            email=email,
            is_active=True,
            is_superuser=admin,
            is_staff=admin
        )
        user.set_password(password)
        return user

    def criaExperiencia(self, nome: str)->Experiencias:
        return Experiencias.objects.create(
            nome=nome,
            subnome = "teste subnome",
            desc= "teste desc",
            data_inicio = datetime.now() - timedelta(days=30),
            data_fim = datetime.now() - timedelta(days=1),
            tags = "Teste Teste_dois Teste_tres"
        )

    def get_tokens_for_user(self, user)->Dict[str, str]:
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }