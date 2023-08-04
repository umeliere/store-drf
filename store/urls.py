from django.urls import path, include
from rest_framework import routers

from store.views import (
    ProductsWithDiscountViewSet,
    ProductsWithoutDiscountViewSet,
    ReviewsViewSet,
)

router = routers.SimpleRouter()
router.register(r'products', ProductsWithoutDiscountViewSet, basename='Products')
router.register(r'discounts', ProductsWithDiscountViewSet, basename='Discounts')
router.register(r'reviews', ReviewsViewSet, basename='Reviews')

app_name = 'store'
urlpatterns = [
    path('', include(router.urls))
]
