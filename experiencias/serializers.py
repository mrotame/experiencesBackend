from rest_framework import serializers
from .models import Experiencias

class ExperienciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencias
        fields = [
            'id',
            'nome',
            'subnome',
            'desc',
            'data_inicio',
            'data_fim',
            'tags'
        ]