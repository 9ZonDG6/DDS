from typing import Any

from rest_framework import serializers as rest_serializers

from apps.core import models, serializers


class CashFlow(rest_serializers.ModelSerializer):
    status_id = rest_serializers.PrimaryKeyRelatedField(
        source='status',
        queryset=models.Status.objects.all(),
        write_only=True,
        required=False,
    )
    status = serializers.Status(read_only=True)
    flow_type_id = rest_serializers.PrimaryKeyRelatedField(
        source='flow_type',
        queryset=models.FlowType.objects.all(),
        write_only=True,
    )
    flow_type = serializers.FlowType(read_only=True)
    category_id = rest_serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=models.Category.objects.select_related('flow_type').all(),
        write_only=True,
    )
    category = serializers.CategoryShort(read_only=True)
    subcategory_id = rest_serializers.PrimaryKeyRelatedField(
        source='subcategory',
        queryset=models.SubCategory.objects.select_related('category').all(),
        write_only=True,
    )
    subcategory = serializers.SubCategoryShort(read_only=True)

    class Meta:
        model = models.CashFlow
        fields = (
            'id',
            'amount',
            'status_id',
            'status',
            'flow_type_id',
            'flow_type',
            'category_id',
            'category',
            'subcategory_id',
            'subcategory',
            'comment',
            'created_at',
        )

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        category = attrs['category']
        subcategory = attrs['subcategory']
        flow_type = attrs['flow_type']
        if category.flow_type != flow_type:
            raise rest_serializers.ValidationError('Категория не относится к выбранному типу.')
        if subcategory.category != category:
            raise rest_serializers.ValidationError('Подкатегория не относится к выбранной категории.')
        return attrs
