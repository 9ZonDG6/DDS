REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '25/minute',
    },
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DATE_FORMAT': '%d.%m.%Y',
    'DATE_INPUT_FORMATS': ['%d.%m.%Y'],
    'DATETIME_FORMAT': '%d.%m.%Y %H:%M:%S%Z',
    'DATETIME_INPUT_FORMATS': ['%d.%m.%Y %H:%M:%S%Z'],
    'DEFAULT_PAGINATION_CLASS': 'config.settings.other.CustomPagination',
    'DEFAULT_RENDERER_CLASSES': ('drf_standardized_response.renderers.StandardizedJSONRenderer',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'drf_standardized_errors.handler.exception_handler',
}
