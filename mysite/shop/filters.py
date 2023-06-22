import django_filters
from django_filters.rest_framework import FilterSet

from shop.models import Product


class ProductFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    minPrice = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    # Greater than or equal to. gte
    maxPrice = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    # Less than or equal to. lte

    class Meta:
        model = Product
        fields = [
            "name", "minPrice", "maxPrice",
        ]
