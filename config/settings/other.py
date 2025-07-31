import sys

from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request


class CustomPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'per_page'

    def get_page_size(self, request: Request) -> int:
        if request.query_params.get(self.page_size_query_param) == 'all':
            return 10000
        else:
            return super().get_page_size(request)
