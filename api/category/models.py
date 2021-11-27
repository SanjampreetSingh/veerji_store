from django.db import models

from utils.model_utils.models import (
    TimeStampedModel
)


class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name