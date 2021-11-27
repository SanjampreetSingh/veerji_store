from django.db import models


from utils.model_utils.models import (
    TimeStampedModel
)


class Locality(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
