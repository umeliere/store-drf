from django.urls import path, include
from rest_framework import routers

from cart.views import CartViewSet, CartItemView

router = routers.SimpleRouter()
router.register(r'', CartViewSet, basename='cart_detail')

app_name = 'cart'
urlpatterns = [
    path('', include(router.urls)),
    path('cart-item/<int:pk>/', CartItemView.as_view()),
]
