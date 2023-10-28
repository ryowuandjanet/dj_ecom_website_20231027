from django.urls import path
from .views import (
  Home,
  ProductDetail
)

urlpatterns = [
  path('',Home.as_view(),name='home'),
  path('product-details/',ProductDetail.as_view(),name='product-details')
]