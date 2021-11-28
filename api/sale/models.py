from django.db import models

from api.product.models import Product
from api.customer.models import Customer

from utils.model_utils.models import (
    TimeStampedModel
)


class Sales(TimeStampedModel, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
