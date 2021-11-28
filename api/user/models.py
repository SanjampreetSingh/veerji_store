from django.db import models
from django.contrib.auth.models import AbstractUser

from api.locality.models import Locality
from utils.model_utils.models import (
    TimeStampedModel
)


class User(TimeStampedModel, AbstractUser):
    name = models.CharField(max_length=50, required=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    house_number = models.CharField(max_length=10)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    session_token = models.CharField(max_length=10, default=0)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
