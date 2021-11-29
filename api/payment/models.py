from django.db import models

from api.user.models import user
from utils.model_utils.models import (
    TimeStampedModel
)


class Payment(TimeStampedModel, models.Model):
    customer = models.ForeignKey(user, on_delete=models.CASCADE)
    payments = models.IntegerField()

    class Meta:
        db_table = "vj_payment"
        verbose_name_plural = "Payments"
