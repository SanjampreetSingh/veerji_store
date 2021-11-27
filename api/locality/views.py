from rest_framework import viewsets

from .serializers import LocalitySerializer
from .models import Locality


class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all().order_by('name')
    serializer_class = LocalitySerializer
