import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Product
        fields = ['sku', 'title', 'description']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            django_filters(title__icontains=value) |
            django_filters(description__icontains=value)
        )

    def multiple_field_search(self, queryset, name, value):
        return queryset.filter(
                queryset(sku__icontains=value) | queryset(title__icontains=value) | queryset(description__icontains=value)
            )
    