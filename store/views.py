from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from store.models import Product, Review
from store.permissions import IsOwnerOrReadOnly
from store.serializers import (
    ProductsSerializer,
    ReviewCreateSerializer,
)
from store.service import ProductFilter


class ProductsWithDiscountViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ProductsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.exclude(Q(discount=0) | Q(is_available=False))


class ProductsListWithoutDiscountView(ListModelMixin, GenericViewSet):
    serializer_class = ProductsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(discount=0, is_available=True)


class ReviewsViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ProductDetailViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
