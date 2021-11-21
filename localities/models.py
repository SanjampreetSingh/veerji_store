from django.db import models
from django.db.models.fields import CharField

from utils.model_utils.models import (
    TimeStampedModel
)


class Localities(TimeStampedModel, models.Model):
    name = CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
