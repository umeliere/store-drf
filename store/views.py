from rest_framework import generics

from store.models import Product, Review
from store.serializers import ProductsListSerializer, ReviewCreateSerializer


class ProductsListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ReviewCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
