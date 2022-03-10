from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False
    )
    category_name = serializers.CharField(
        source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'image', 'category', 'category_name'
        )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'name'
        )
