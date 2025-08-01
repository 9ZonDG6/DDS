from rest_framework import viewsets

from apps.core import filters, models, serializers


class CashFlow(viewsets.ModelViewSet):
    """
    Управление денежными потоками
    """

    serializer_class = serializers.CashFlow
    queryset = models.CashFlow.objects.select_related('status', 'flow_type', 'category', 'subcategory').order_by(
        '-created_at'
    )
    filterset_class = filters.CashFlow
