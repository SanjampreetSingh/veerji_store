from django.db import models

from api.user.models import User
from utils.model_utils.models import (
    TimeStampedModel
)


class RecurringProduct(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.JSONField()

    class Meta:
        db_table = "vj_recurring_product"
        verbose_name_plural = "RecurringProducts"
