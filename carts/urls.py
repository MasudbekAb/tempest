from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug:product_slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
]
