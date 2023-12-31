from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from store.models import Product, Review
from store.permissions import IsOwnerOrReadOnly
from store.serializers import (
    ProductsSerializer,
    ReviewCreateSerializer,
)
from store.service import ProductFilter, ProductsApiPagination


class ProductsWithDiscountViewSet(ListModelMixin, GenericViewSet):
    """
    The products with the discount view
    """
    serializer_class = ProductsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = ProductsApiPagination

    def get_queryset(self):
        return Product.objects.exclude(Q(discount=0) | Q(is_available=False))


class ProductsWithoutDiscountViewSet(ListModelMixin, GenericViewSet):
    """
    The products without any discount view
    """
    serializer_class = ProductsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = ProductsApiPagination

    def get_queryset(self):
        return Product.objects.filter(discount=0, is_available=True)

    @action(methods=['get'], detail=True)
    def product(self, request, pk=None):
        """
        Method returns the detail product
        """
        queryset = get_object_or_404(Product, pk=self.kwargs['pk'])
        serializer_for_queryset = ProductsSerializer(
            instance=queryset,
        )
        return Response(serializer_for_queryset.data)


class ReviewsViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    The reviews view, allows use CRUD
    """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
