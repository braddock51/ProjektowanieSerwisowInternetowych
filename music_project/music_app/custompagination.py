from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response

    
class PageNumberPaginationDataOnly(PageNumberPagination):
    max_limit = 10

    def get_paginated_response(self, data):
        return Response(data)