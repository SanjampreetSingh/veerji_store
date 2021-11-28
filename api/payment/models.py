from django.db import models

from api.customer.models import Customer
from utils.model_utils.models import (
    TimeStampedModel
)


class Payment(TimeStampedModel, models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payments = models.IntegerField()
