from django.db import models

from customers.models import Customers

class Payments(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    payments = models.IntegerField()