from itertools import product as itertools_product  # Переименование функции product

from django.shortcuts import render
from goods.models import Aproduct, products

def productsView(request):
    products_list = products.objects.all()  # Используйте правильное имя модели
    context = {
        'title': 'Products - catalog',
        'products': products_list,
    }
    return render(request, 'goods/products.html', context)

def AproductView(request):
    product_list = Aproduct.objects.all()  # Переименуйте переменную, чтобы она не конфликтовала с моделью
    context = {
        'title': 'Products - catalog',
        'products': product_list,
    }
    return render(request, 'goods/product.html', context)
