from django.db import models

from api.product.models import Product
from api.user.models import User

from utils.model_utils.models import (
    TimeStampedModel
)


class Sale(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "vj_sale"
        verbose_name_plural = "Sales"
