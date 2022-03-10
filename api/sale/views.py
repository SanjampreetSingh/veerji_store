import json
from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

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


class GetSalePerUser(generics.RetrieveAPIView):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        try:
            year = str(self.kwargs['year'])
            month = str(self.kwargs['month'])
            sale = Sale.objects.all().filter(
                user=str(request.user.id)
            ).filter(
                created__year__gte=year,
                created__month__gte=month,
                created__year__lte=year,
                created__month__lte=month
            )
        except(Sale.DoesNotExist):
            sale = None

        if sale is not None:
            serializer = SaleSerializer(sale, many=True)
            return Response(data=serializer.data)
        else:
            return res.respond_error(error_message='Invalid user.')
