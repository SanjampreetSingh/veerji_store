from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import RecurringProductSerializer
from .models import RecurringProduct


class RecurringProductViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create': [AllowAny],
    }

    queryset = RecurringProduct.objects.all().order_by('id')
    serializer_class = RecurringProductSerializer
    lookup_field = "user"

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]
