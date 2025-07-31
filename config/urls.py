from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/')),
    path('backend/', include('apps.core.urls', namespace='core')),
    path('backend/admin/', admin.site.urls),
    path('backend/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('backend/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('backend/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('backend/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.ENABLE_SILK:
    urlpatterns += [
        path('backend/silk/', include('silk.urls', namespace='silk')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
