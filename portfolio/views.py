from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import PageSection, SectionContent, Category
from .serializers import PageSectionSerializer, CategorySerializer, AlbumCategorySerializer

@method_decorator(cache_page(5), name='dispatch')
class PageSectionContentView(generics.ListAPIView):
    queryset = PageSection.objects.prefetch_related('content_items').order_by('order')
    serializer_class = PageSectionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


class CategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@method_decorator(cache_page(5), name='dispatch')
class Album(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = AlbumCategorySerializer
    pagination_class = CategoryPagination
    lookup_field = 'slug'