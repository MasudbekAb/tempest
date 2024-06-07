# orders/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order, OrderItem
from carts.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from .forms import OrderForm

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user

            cart_items = CartItem.objects.filter(cart__user=request.user)
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            order.total_price = total_price
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
            cart_items.delete()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Order

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})