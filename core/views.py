from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Menu, Footer, QuickLink, FooterText, PageSection, SectionContent

from .serializers import (
    HeaderFooterSerializer,
    QuickLinkSerializer,
    FooterTextSerializer,
    MenuSerializer,
    FooterSerializer,
    PageSectionSerializer,
)

class HeaderFooterView(APIView):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.filter(is_active=True).order_by('order')
        
        footer = Footer.objects.first()

        quick_links = QuickLink.objects.all()
        footer_text = FooterText.objects.first()

        menu_serializer = MenuSerializer(menus, many=True)
        footer_serializer = FooterSerializer(footer)
        quick_link_serializer = QuickLinkSerializer(quick_links, many=True)
        footer_text_serializer = FooterTextSerializer(footer_text)

        data = {
            'menus': menu_serializer.data,
            'footer': footer_serializer.data,
            'quick_links': quick_link_serializer.data,
            'made_with_text': footer_text_serializer.data['made_with_text'],
        }
        
        return Response(data, status=status.HTTP_200_OK)


@method_decorator(cache_page(60 * 15), name='dispatch')
class PageSectionContentView(generics.ListAPIView):
    queryset = PageSection.objects.prefetch_related('content_items').order_by('order')
    serializer_class = PageSectionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset.filter(is_active=True)