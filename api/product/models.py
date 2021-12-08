from django.db import models

from utils.model_utils.models import (
    TimeStampedModel
)
from api.category.models import Category


class Product(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(
        upload_to='images/product/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name + " - " + self.price

    class Meta:
        db_table = "vj_product"
        verbose_name_plural = "Products"
