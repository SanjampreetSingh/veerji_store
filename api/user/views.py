import random
import re
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend


from .serializer import UserSerializer
from .models import User
from utils.response_utils import ResponseUtils as res


def generate_session_token(lenght=10):
    return ''.join(random.SystemRandom().choice(
        [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    ) for _ in range(lenght))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return res.respond_error(
            details='error',
            error_message='Send a POST request with valid parameter only'
        )

    username = request.POST['email']
    password = request.POST['password']

    # Validation part
    if not re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', username):
        return res.respond_error(
            details='error',
            error_message='Enter a valid email'
        )

    if len(password) < 8:
        return res.respond_error(
            details='error',
            error_message='Password need to be atleast 8 characters'
        )

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            user_dict = UserModel.objects.filter(
                email=username).values().first()
            user_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return res.respond_error(
                    details='error',
                    error_message='Previous session exists'
                )

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return res.respond_data(
                data={
                    'token': token,
                    'user': user_dict
                }
            )
        else:
            return res.respond_error(
                details='error',
                error_message='Invalid password'
            )

    except UserModel.DoesNotExist:
        return res.respond_error(
            details='error',
            error_message='Invalid email'
        )


def signout(request, id) -> None:
    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return res.respond_error(
            details='error',
            error_message='Invalid email'
        )

    return res.respond_success(success_message='Logout success')


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends= [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['locality']
    search_fields = ['phone', 'email', 'name', 'house_number']
    ordering_fields = ['name', 'phone', 'house_number']
    ordering = ['id']

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]
