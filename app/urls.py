from django.urls import path
from . import views
from app.views import ApiHomePage

urlpatterns = [
    path('products/', ApiHomePage.as_view(), name='all_products'),
    path('products/<int:id>', ApiHomePage.as_view(), name='product_by_id'),
]