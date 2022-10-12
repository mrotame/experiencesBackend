from django.urls import path
from .views import Experiencias
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',Experiencias.as_view(), name='experiencias'),
    path('<int:id>/',Experiencias.as_view(), name='experiencias'),
]

