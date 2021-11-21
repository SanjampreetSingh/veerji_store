from django.db import models
from django.db.models.fields import CharField



class Localities(models.Model):
    name = CharField(max_length=300)

    def __str__(self) -> str:
        return self.name