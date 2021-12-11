from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import LocalitySerializer
from .models import Locality


class LocalityViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
    queryset = Locality.objects.all().order_by('name')
    serializer_class = LocalitySerializer

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]
