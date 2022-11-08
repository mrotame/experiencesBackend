from rest_framework import generics
from rest_framework.response import Response
from main.default_permissions.isAdmin import IsAdmin
from ..serializers import ExperienciasSerializer
from ..models import Experiencias
from ..listaExperiencias import ListaExperiencias
from datetime import datetime

class UpdateAllGenericView(generics.GenericAPIView):
    # queryset = Experiencias
    permission_classes = [IsAdmin]
    
    def post(self, request, *args, **kwargs):
        for item in ListaExperiencias().todas:

            experiencia = Experiencias.objects.create(
                nome = item.get("nome"),
                subnome = item.get("subnome"),
                desc = self.descClean(item.get("desc")),
                data_inicio = self.strptime(item.get("data_inicio")),
                data_fim = self.strptime(item.get("data_fim")),
                tags = self.listToString(item.get('tags'))
            )
        return Response({"msg":"ok"}, 200)

    def strptime(self, string:str):
        if string == '':
            return None
        time_format = '%Y/%m'
        return datetime.strptime(string, time_format)

    def listToString(self, lista: list):
        return ' '.join(lista)

    def descClean(self, desc:str):
        return desc.replace("  ", "").replace("\n ", "\n")
