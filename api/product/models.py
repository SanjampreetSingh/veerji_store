from django.db import models

from utils.model_utils.models import (
    TimeStampedModel
)


class Product(TimeStampedModel, models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " - " + str(self.cost)
