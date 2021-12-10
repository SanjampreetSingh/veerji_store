from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from api.locality.models import Locality
from utils.model_utils.models import (
    TimeStampedModel
)
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    phone = models.CharField(max_length=15)
    house_number = models.CharField(max_length=8)
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)
    username = None
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'house_number', 'locality']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "vj_user"
        verbose_name_plural = "Users"
