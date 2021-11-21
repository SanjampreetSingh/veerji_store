from django.db import models
from django.db.models.fields import CharField


from localities.models import Localities


class Customers(models.Model):
    name = CharField(max_length=60)
    contact = CharField(max_length=13)
    house_number = CharField(max_length=7)
    locality = models.ForeignKey(Localities, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + " - " + self.house_number
