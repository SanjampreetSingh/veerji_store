from django.db import models

from customers.models import Customers
from utils.model_utils.models import (
    TimeStampedModel
)


class Payments(TimeStampedModel, models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    payments = models.IntegerField()
