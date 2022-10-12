from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Experiencias(models.Model):
    nome: str = models.CharField(max_length=200)
    subnome: str = models.CharField(max_length=200)
    desc: str = models.TextField()
    data_inicio: str = models.DateField()
    data_fim: datetime = models.DateField()
    tags: datetime = models.CharField(max_length=2000)
    data_criacao: datetime = models.DateField(default=timezone.now)