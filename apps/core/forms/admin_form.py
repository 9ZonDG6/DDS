from typing import Any

from dal import autocomplete
from django import forms

from apps.core import models


class CashFlowAdmin(forms.ModelForm):
    class Meta:
        model = models.CashFlow
        fields = (
            'amount',
            'status',
            'flow_type',
            'category',
            'subcategory',
            'comment',
            'created_at',
        )

        widgets = {
            'category': autocomplete.ModelSelect2(
                url='core:category-autocomplete',
                forward=['flow_type'],
            ),
            'subcategory': autocomplete.ModelSelect2(
                url='core:subcategory-autocomplete',
                forward=['category'],
            ),
        }

    def clean(self) -> dict[str, Any]:
        cleaned = super().clean()
        flow_type = cleaned.get('flow_type')
        category = cleaned.get('category')
        subcategory = cleaned.get('subcategory')

        if category and flow_type and category.flow_type_id != flow_type.id:
            self.add_error('category', 'Категория не относится к выбранному типу.')
        if subcategory and category and subcategory.category_id != category.id:
            self.add_error('subcategory', 'Подкатегория не относится к выбранной категории.')
        return cleaned
