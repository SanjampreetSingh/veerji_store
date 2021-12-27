from django.db import models

from api.user.models import User
from api.product.models import Product
from utils.model_utils.models import (
    TimeStampedModel
)


class Sale(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "vj_sale"
        verbose_name_plural = "Sales"
