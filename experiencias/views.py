from .models import Experiencias as ExperienciasModel
from .serializers import ExperienciasSerializer
from rest_framework import generics, mixins
from main.default_permissions.isAdmin import IsAdmin

class ExperienciasGenericView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = ExperienciasModel.objects.all()
    serializer_class = ExperienciasSerializer
    lookup_field = 'id'
    # authentication_classes = []
    #permission_classes = []

    def get(self, request, *args, **kwargs):
        if kwargs.get('id') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
    def get_permissions(self):
        if self.request.method != 'GET':
            permission_classes = [IsAdmin]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]