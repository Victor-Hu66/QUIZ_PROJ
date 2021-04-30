from rest_framework.pagination import PageNumberPagination

# Custom pagination (global için settings'e git)
class MyPagination(PageNumberPagination):
    page_size = 1