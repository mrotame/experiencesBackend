from rest_framework.generics import GenericAPIView, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from users.models.users import Users
from ..serializers import UserSerializer
from main.default_permissions.isAdmin import IsAdmin
from main.default_permissions.isOwner import IsOwner

class UsersGenericView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
    ):

    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def validate(self):
        if self.request.method != 'GET' and "id" not in self.kwargs:
            raise ValidationError({"error": "invalid URL"}, 400)

    def get_queryset(self):
        self.validate()
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        if kwargs.get('id') is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_permissions(self):
        permission_classes = [(IsOwner| IsAdmin)]
        if self.request.method == 'GET' and self.kwargs.get('id') == None:
                permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]