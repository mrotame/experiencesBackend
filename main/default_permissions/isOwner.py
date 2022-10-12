from lib2to3.pytree import Base
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.kwargs.get('id') == request.user.id:
            return True
        return False