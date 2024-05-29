from django.urls import path
from goods import views 

urlpatterns = [
    path('', views.products, name='products'),
    path('product/', views.product, name='product'),
]
