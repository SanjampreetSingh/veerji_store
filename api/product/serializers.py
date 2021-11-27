from rest_framework import serializers

from .models import ProdProduct


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = '__all__'