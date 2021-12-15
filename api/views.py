from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime
from rest_framework.decorators import api_view

from utils.response_utils import ResponseUtils as res


@api_view(['GET'])
def checkserver(request):
    message = 'Server is live at ' + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return res.respond_success(details=message)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if user.is_superuser == True:
            token['type'] = 1
        else:
            token['type'] = 2

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
