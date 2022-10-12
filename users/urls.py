from django.urls import path
from .views.users import UsersGenericView

urlpatterns = [
    path('', UsersGenericView.as_view(), name="users generic view"),
    path('<int:id>/', UsersGenericView.as_view(), name="users generic view id based")
]
