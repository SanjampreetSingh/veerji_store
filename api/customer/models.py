from django.db import models


from api.locality.models import Locality
from utils.model_utils.models import (
    TimeStampedModel
)


class Customer(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    house_number = models.CharField(max_length=7)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + " - " + self.house_number
