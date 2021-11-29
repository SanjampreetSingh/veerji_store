from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from .serializers import SaleSerializer
from .models import Sale
from utils.response_utils import ResponseUtils as res


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('id')
    serializer_class = SaleSerializer


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return res.respond_error(
            details='error',
            error_message='Please re-login'
        )

    if not request.method == "POST":
        return res.respond_error(
            details='error',
            error_message='Send a POST request with valid parameter only'
        )

    transaction_id = request.POST['transaction_id']
    amount = request.POST['amount']
    products = request.POST['products']

    total_product = len(products.split(',')[:-1])

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return res.respond_error(
            details='error',
            error_message='User does not exist'
        )

    sale = Sale(
        user=user,
        product_name=products,
        total_product=total_product,
        transaction_id=transaction_id,
        total_amount=amount
    )

    sale.save()
    return res.respond_success(success_message='Sales added')
