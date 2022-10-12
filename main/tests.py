from typing import Dict
from django.test import TestCase
from users.models.users import Users
from rest_framework_simplejwt.tokens import RefreshToken
from users.views.users import UsersGenericView
from experiencias.views import ExperienciasGenericView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class DefaultTestCase(TestCase):
    usersView = (UsersGenericView.as_view(), '/usuarios')
    experienciasView = (ExperienciasGenericView, '/experiencias')
    sessionTokenView = (TokenObtainPairView.as_view(), '/token')
    sessionRefreshView = (TokenRefreshView.as_view(), '/refresh')

    def criaUsuario(self, email:str, password="12345", admin:bool=False)->Users:
        user = Users.objects.create(
            email=email,
            is_active=True,
            is_superuser=admin,
            is_staff=admin
        )
        user.set_password(password)
        return user

    def get_tokens_for_user(self, user)->Dict[str, str]:
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }