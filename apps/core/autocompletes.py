from dal import autocomplete
from django.db.models.query import QuerySet

from apps.core import models


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    """Категории, автоматически отфильтрованные по типу денежного движения."""

    def get_queryset(self) -> QuerySet[models.Category]:
        qs = models.Category.objects.select_related('flow_type').all()
        flow_type_id = self.forwarded.get('flow_type')
        return qs.filter(flow_type_id=flow_type_id) if flow_type_id else qs.none()


class SubCategoryAutocomplete(autocomplete.Select2QuerySetView):
    """Подкатегории, автоматически отфильтрованные по категории денежного движения."""

    def get_queryset(self) -> QuerySet[models.SubCategory]:
        qs = models.SubCategory.objects.select_related('category').all()
        category_id = self.forwarded.get('category')
        return qs.filter(category_id=category_id) if category_id else qs.none()
