import random
import re
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt


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
