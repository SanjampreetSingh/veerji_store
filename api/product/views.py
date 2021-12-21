from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import ProductSerializer, ProductListSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
    queryset = Product.objects.all().order_by('category')
    serializer_class = ProductSerializer

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
