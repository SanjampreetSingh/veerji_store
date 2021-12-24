from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken


from .serializer import UserSerializer
from .models import User
from utils.response_utils import ResponseUtils as res


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'list': [IsAdminUser],
        'retrieve': [IsAdminUser],
        'create': [AllowAny],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['locality']
    search_fields = ['=phone', '=email', 'name', 'house_number']
    ordering_fields = ['name', 'phone', 'house_number']
    ordering = ['id']

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return res.respond_success()

        except Exception as e:
            return res.respond_error(error_message=e.message)
