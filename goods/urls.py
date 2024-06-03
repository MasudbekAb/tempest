from django.urls import path
from goods import views 

urlpatterns = [
    path('', views.productsView, name='products'),
    path('product/', views.AproductView, name='product'),
]
