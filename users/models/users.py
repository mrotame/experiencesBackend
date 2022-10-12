from ..usersManager import UserManager
from typing import List
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import EmailValidator
from softdelete.models import SoftDeleteObject

class Users(AbstractBaseUser,SoftDeleteObject, PermissionsMixin):
    nome: str = models.CharField(_("name"),max_length=100, blank=True, null=True)
    email: str = models.EmailField(_("email address"),max_length=255, unique=True, blank=False, null=False)
    data_registro = models.DateTimeField(_("register date"), default=timezone.now)
    password: str = models.CharField(_("User's password"), max_length=256, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List[str] = [password]

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)