from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from api.locality.models import Locality
from utils.model_utils.models import (
    TimeStampedModel
)
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    phone = models.CharField(max_length=15)
    payment = models.IntegerField(null=True, default=0)
    recurring_product = models.TextField(default="[]")
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)
    house_number = models.CharField(max_length=8)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'house_number']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]

    class Meta:
        db_table = "vj_user"
        verbose_name_plural = "Users"
