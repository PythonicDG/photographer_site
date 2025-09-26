from django.urls import path
from .views import PageSectionContentView, Album

urlpatterns = [
    path('api/fetch-portfolio_page/', PageSectionContentView.as_view(), name='page-section-content-list'),
    path('api/album/<slug:slug>/', Album.as_view(), name='album')
]
