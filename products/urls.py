from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.get_product, name='get_product'),
]
