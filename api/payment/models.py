from django.db import models

from api.user.models import User
from utils.model_utils.models import (
    TimeStampedModel
)


class Payment(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payments = models.CharField(max_length=10)

    class Meta:
        db_table = "vj_payment"
        verbose_name_plural = "Payments"
