from django.shortcuts import render, redirect, get_object_or_404
from goods.models import Aproduct

def add_to_cart(request, product_slug):
    product = get_object_or_404(Aproduct, slug=product_slug)
    cart = request.session.get('cart', {})
    cart[product_slug] = cart.get(product_slug, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_slug):
    cart = request.session.get('cart', {})
    if product_slug in cart:
        del cart[product_slug]
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = Aproduct.objects.filter(slug__in=cart.keys())
    total = sum(product.price * cart[str(product.slug)] for product in cart_items)
    return render(request, 'carts/cart.html', {'cart_items': cart_items, 'total': total})



