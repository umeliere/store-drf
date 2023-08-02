from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet
from rest_framework.pagination import PageNumberPagination

from store.models import Product


class CharFilterInFilter(BaseInFilter, CharFilter):
    """
    Filter class for multiple uses
    read docs: https://django-filter.readthedocs.io/en/stable/ref/filters.html
    """
    pass


class ProductsApiPagination(PageNumberPagination):
    """
    Modified pagination class for Product model
    """
    page_size = 12


class ProductFilter(FilterSet):
    """
    Filter class for filter by category
    """
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ('category',)
