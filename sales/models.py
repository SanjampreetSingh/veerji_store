from django.db import models

from products.models import Products
from customers.models import Customers

class Sales(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)