from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    user_phone = serializers.CharField(source="user.phone", read_only=True)

    class Meta:
        model = Sale
        fields = (
            'id', 'user', 'product', 'quantity',
            'product_name', 'user_name', 'user_phone',
            'created'
        )
