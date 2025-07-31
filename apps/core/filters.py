from django_filters import rest_framework as django_filters

from apps.core import models


class CashFlow(django_filters.FilterSet):
    status = django_filters.BaseInFilter(field_name='status__id', label='Статус')
    flow_type = django_filters.BaseInFilter(field_name='flow_type__id', label='Тип')
    category = django_filters.BaseInFilter(field_name='category__id', label='Категория')
    subcategory = django_filters.BaseInFilter(field_name='subcategory__id', label='Подкатегория')
    created_at_from = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = models.CashFlow
        fields = ('status', 'flow_type', 'category', 'subcategory', 'created_at_from', 'created_at_to')
