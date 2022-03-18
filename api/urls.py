from django.urls import path, include
from .views import checkserver, MyTokenObtainPairView
from api.locality.views import LocalityList
from api.product.views import ProductList
from api.user.views import UserList, UserGetUser, start_payment
from api.sale.views import add_recurring_product, GetSalePerUser, FilterSaleByDate

urlpatterns = [
    path('', checkserver, name='api.checkserver'),
    path('category/', include('api.category.urls')),
    path('locality/', include('api.locality.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('sale/', include('api.sale.urls')),
    path(
        'token/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('list/locality/', LocalityList.as_view(), name='locality-list'),
    path('list/product/', ProductList.as_view(), name='product-list'),
    path('list/user/', UserList.as_view(), name='user-list'),
    path('get/user/', UserGetUser.as_view(), name='user-retrieve'),
    path(
        'add/sale/recurring_product/',
        add_recurring_product,
        name='sale.add_recurring_product'
    ),
    path(
        'get/sale_per_user/<month>/<year>/',
        GetSalePerUser.as_view(),
        name='sale.sale_per_user'
    ),
    path(
        'filter/sale_by_date/<date>/',
        FilterSaleByDate.as_view(),
        name='sale.sale_by_date'
    ),
    path('pay/', start_payment, name="payment"),
]
