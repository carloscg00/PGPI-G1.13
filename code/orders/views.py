from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html', locals())
    else:
        form = OrderCreateForm()
    return render(request,
        'orders/order/create.html',
        {'cart': cart, 'form': form})

@login_required
def my_orders(request):
    orders = OrderItem.objects.all()
    order_list = []
    for o in orders:
        if o.order.first_name == request.user.first_name and o.order.last_name == request.user.last_name:
            order_list.append(o)
    return render(request, 'my_orders.html', {'orders': order_list})