from django.urls import path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from apps.core import autocompletes, views

app_name = 'core'

router = DefaultRouter()

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/swagger/')),
    path('backend/autocomplete/category/', autocompletes.CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path(
        'backend/autocomplete/subcategory/',
        autocompletes.SubCategoryAutocomplete.as_view(),
        name='subcategory-autocomplete',
    ),
]

router.register('cashflow', views.CashFlow, basename='cashflow')
router.register('status', views.Status, basename='status')
router.register('type', views.FlowType, basename='type')
router.register('category', views.Category, basename='category')
router.register('subcategory', views.SubCategory, basename='subcategory')

urlpatterns += router.urls
