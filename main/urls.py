from django.urls import path
from .views.index import Index

urlpatterns = [
    path("",Index.as_view(), name='index')
]

