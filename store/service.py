from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet

from store.models import Product


class CharFilterInFilter(BaseInFilter, CharFilter):
    """
    filter class for multiple uses
    read docs: https://django-filter.readthedocs.io/en/stable/ref/filters.html
    """
    pass


class ProductFilter(FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ('category',)
