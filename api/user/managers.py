from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from api.locality.models import Locality


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, name, phone, house_number, password, **extra_fields):
        if not email:
            raise ValueError(_('An email must be provided'))

        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, phone=phone,
            house_number=house_number, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, name, phone, house_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, house_number, password, **extra_fields)

    def create_superuser(self, email, name, phone, house_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('locality', Locality.objects.get(pk=1))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, name, phone, house_number, password, **extra_fields)
