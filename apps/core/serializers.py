from typing import Any

from rest_framework import serializers

from apps.core import models


class Status(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ('id', 'name')


class FlowType(serializers.ModelSerializer):
    class Meta:
        model = models.FlowType
        fields = ('id', 'name')


class Category(serializers.ModelSerializer):
    flow_type_id = serializers.PrimaryKeyRelatedField(
        source='flow_type',
        queryset=models.FlowType.objects.all(),
        write_only=True,
    )
    flow_type = FlowType(read_only=True)

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'flow_type_id', 'flow_type')


class CategoryShort(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class SubCategory(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=models.Category.objects.select_related('flow_type').all(),
        write_only=True,
    )
    category = CategoryShort(read_only=True)

    class Meta:
        model = models.SubCategory
        fields = ('id', 'name', 'category_id', 'category')


class SubCategoryShort(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ('id', 'name')


class CashFlow(serializers.ModelSerializer):
    status_id = serializers.PrimaryKeyRelatedField(
        source='status',
        queryset=models.Status.objects.all(),
        write_only=True,
        required=False,
    )
    status = Status(read_only=True)
    flow_type_id = serializers.PrimaryKeyRelatedField(
        source='flow_type',
        queryset=models.FlowType.objects.all(),
        write_only=True,
    )
    flow_type = FlowType(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=models.Category.objects.select_related('flow_type').all(),
        write_only=True,
    )
    category = CategoryShort(read_only=True)
    subcategory_id = serializers.PrimaryKeyRelatedField(
        source='subcategory',
        queryset=models.SubCategory.objects.select_related('category').all(),
        write_only=True,
    )
    subcategory = SubCategoryShort(read_only=True)

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
            raise serializers.ValidationError('Категория не относится к выбранному типу.')
        if subcategory.category != category:
            raise serializers.ValidationError('Подкатегория не относится к выбранной категории.')
        return attrs
