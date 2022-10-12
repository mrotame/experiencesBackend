from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from softdelete.models import SoftDeleteManager
# Create your models here.
class UserManager(BaseUserManager, SoftDeleteManager):
    use_in_migrations = True

    def create_user(self, email:str, password:str, nome:str='', **extra_fields):

        if not email:
            raise ValueError(_('The given email must be set'))

        email = self.normalize_email(email)
        user = self.model(nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self.create_user(email, password, **extra_fields)
