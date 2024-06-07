# orders/urls.py

from django.urls import path
from .views import create_order, order_detail, order_list

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('<int:order_id>/', order_detail, name='order_detail'),
    path('all/', order_list, name='order_list'),
]
