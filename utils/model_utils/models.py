from django.utils.translation import gettext_lazy as _
from django.db import models
from .fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)

from django.db.models.functions import Now
now = Now()


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        if 'update_fields' in kwargs and\
                'modified' not in kwargs['update_fields']:
            kwargs['update_fields'] += ['modified']
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
