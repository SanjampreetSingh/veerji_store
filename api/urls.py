from django.urls import path, include
from .views import checkserver, MyTokenObtainPairView

urlpatterns = [
    path('', checkserver, name='api.checkserver'),
    path('category/', include('api.category.urls')),
    path('locality/', include('api.locality.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('sale/', include('api.sale.urls')),
    path('recurring_product/', include('api.recurring_product.urls')),
    path(
        'token/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

]
