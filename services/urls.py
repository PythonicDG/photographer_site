from django.urls import path
from .views import PageSectionContentView

urlpatterns = [
    path('api/fetch-service_page/', PageSectionContentView.as_view(), name='page-section-content-list'),
]
