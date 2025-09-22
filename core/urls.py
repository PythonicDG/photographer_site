from django.urls import path
from .views import HeaderFooterView, PageSectionContentView

urlpatterns = [
    path('api/header-footer/', HeaderFooterView.as_view(), name='header-footer'),
    path('api/fetch-home_page/', PageSectionContentView.as_view(), name='page-section-content-list'),
]
