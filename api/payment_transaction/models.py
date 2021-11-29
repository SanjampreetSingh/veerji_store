from django.db import models

from utils.model_utils.models import (
    TimeStampedModel
)


class PaymentTransaction(TimeStampedModel, models.Model):
    pass
