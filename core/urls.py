from django.urls import path
from .views import HeaderFooterView

urlpatterns = [
    path('api/header-footer/', HeaderFooterView.as_view(), name='header-footer'),
]
