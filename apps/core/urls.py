from django.urls import path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from apps.core import autocompletes, views

app_name = 'core'

router = DefaultRouter()

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/swagger/')),
    path('autocomplete/category/', autocompletes.CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path(
        'autocomplete/subcategory/',
        autocompletes.SubCategoryAutocomplete.as_view(),
        name='subcategory-autocomplete',
    ),
]

router.register('cashflows', views.CashFlow, basename='cashflows')
router.register('statuses', views.Status, basename='statuses')
router.register('types', views.FlowType, basename='types')
router.register('categories', views.Category, basename='categories')
router.register('subcategories', views.SubCategory, basename='subcategories')

urlpatterns += router.urls
