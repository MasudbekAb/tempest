from django.shortcuts import render

def products(request):
    context = {
        'title': 'Products - catalog',
        
    }
    return render(request, 'goods/products.html')


def product(request):
    return render(render, 'goods/product.html')

 
