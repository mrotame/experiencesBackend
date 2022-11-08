from django.urls import path
from .views.experienciasView import ExperienciasGenericView
from rest_framework.authtoken.views import obtain_auth_token
from .views.updateAllView import UpdateAllGenericView

urlpatterns = [
    path('',ExperienciasGenericView.as_view(), name='experiencias'),
    path('<int:id>/',ExperienciasGenericView.as_view(), name='experiencias'),
    path('updateall/', UpdateAllGenericView.as_view())
]

