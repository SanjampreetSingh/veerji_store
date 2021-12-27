import json
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .serializers import SaleSerializer
from .models import Sale
from utils.response_utils import ResponseUtils as res
from api.user.models import User
from api.product.models import Product


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('id')
    serializer_class = SaleSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_recurring_product(request):
    if not request.method == "POST":
        return res.respond_error(
            details='error',
            error_message='Send a POST request with valid parameter only'
        )
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
