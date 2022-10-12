from django.urls import path
from .views import ExperienciasGenericView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',ExperienciasGenericView.as_view(), name='experiencias'),
    path('<int:id>/',ExperienciasGenericView.as_view(), name='experiencias'),
]

