from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " - " + self.cost