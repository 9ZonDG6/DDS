from django.contrib import admin
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from apps.core import models
from apps.core.forms import CashFlowAdmin


@admin.register(models.CashFlow)
class CashFlow(admin.ModelAdmin):
    form = CashFlowAdmin

    list_display = ('id', 'amount', 'status', 'flow_type', 'category', 'subcategory', 'created_at')
    list_select_related = ('status', 'flow_type', 'category', 'subcategory')
    list_filter = (
        'status',
        'flow_type',
        'category',
        'subcategory',
        ('created_at', DateRangeFilter),
    )
    autocomplete_fields = ('status', 'flow_type')


@admin.register(models.Status)
class Status(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.FlowType)
class FlowType(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'flow_type')
    list_select_related = ('flow_type',)
    search_fields = ('name', 'flow_type__name')
    autocomplete_fields = ('flow_type',)


@admin.register(models.SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_select_related = ('category',)
    search_fields = ('name', 'category__name')
    autocomplete_fields = ('category',)


admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
admin.site.unregister(Group)
