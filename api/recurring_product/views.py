from rest_framework import viewsets

from .serializers import RecurringProductSerializer
from .models import RecurringProduct


class RecurringProductViewSet(viewsets.ModelViewSet):
    queryset = RecurringProduct.objects.all().order_by('id')
    serializer_class = RecurringProductSerializer
