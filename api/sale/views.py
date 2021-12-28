import json
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAdminUser

from .models import Sale
from .serializers import SaleSerializer
from utils.response_utils import ResponseUtils as res
from api.user.models import User
from api.product.models import Product


class SaleViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
    queryset = Sale.objects.all().order_by('created')
    serializer_class = SaleSerializer

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_recurring_product(request):
    try:
        users = User.objects.all().exclude(
            recurring_product="[]").values('id', 'recurring_product')
    except Exception as e:
        return res.respond_error(error_message=e.message)

    for user in users:
        user_id = user.get('id')
        products = json.loads(user.get('recurring_product'))
        for product in products:
            product_id = product.get('productId')
            quantity = product.get('quantity')
            try:
                sale = Sale(user=User(pk=user_id), product=Product(
                    pk=product_id), quantity=int(quantity))
                sale.save()
            except Exception as e:
                return res.respond_error(error_message=e.message)
    return res.respond_success(success_message='Recurring sales added')
