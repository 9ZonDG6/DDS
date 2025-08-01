from rest_framework import viewsets

from apps.core import models, serializers


class Status(viewsets.ModelViewSet):
    """
    Справочник статусов
    """

    serializer_class = serializers.Status
    queryset = models.Status.objects.all().order_by('id')


class FlowType(viewsets.ModelViewSet):
    """
    Справочник типов
    """

    serializer_class = serializers.FlowType
    queryset = models.FlowType.objects.all().order_by('id')


class Category(viewsets.ModelViewSet):
    """
    Справочник категорий
    """

    serializer_class = serializers.Category
    queryset = models.Category.objects.select_related('flow_type').all().order_by('id')


class SubCategory(viewsets.ModelViewSet):
    """
    Справочник подкатегорий
    """

    serializer_class = serializers.SubCategory
    queryset = models.SubCategory.objects.select_related('category', 'category__flow_type').all().order_by('id')
