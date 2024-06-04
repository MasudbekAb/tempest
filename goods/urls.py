from django.urls import path
from goods import views 

urlpatterns = [
    path('', views.productsView, name='products'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
     path('search/', views.search_view, name='search'),
     path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('product/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('add-to-favorite/<slug:product_slug>/', views.add_to_favorite, name='add_to_favorite'),
    path('remove-from-favorite/<slug:product_slug>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('favorite/', views.favorite_page, name='favorite_page'),
]
