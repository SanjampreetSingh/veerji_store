from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = (
            'id', 'user',
        )

        #  'product_name', 'total_product', 'transaction_id', 'total_amount', 'product',
