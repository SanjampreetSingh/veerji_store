from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


from .serializer import UserSerializer, UserListSerializer, UserRetrieveSerializer
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
    search_fields = ['phone', 'email', 'name', 'house_number']
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


class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]


class UserGetUser(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(pk=str(request.user.id))
        except(User.DoesNotExist):
            user = None

        if user is not None:
            serializer = UserRetrieveSerializer(user)
            return Response(data=serializer.data)
        else:
            return res.respond_error(error_message='Invalid user.')
