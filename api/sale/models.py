from django.db import models

from api.product.models import Product
from api.user.models import User

from utils.model_utils.models import (
    TimeStampedModel
)


class Sale(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=500)
    total_product = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "vj_sale"
        verbose_name_plural = "Sales"
