from rest_framework import serializers

from .models import RecurringProduct


class RecurringProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecurringProduct
        fields = (
            'id', 'user', 'product'
        )
