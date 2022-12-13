from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import OrderItem
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
            order = form.save(commit=False)
            order.first_name = request.user.first_name
            order.email = request.user.email
            order.save()
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
    lista = []
    u = request.user
    for o in orders:
        if o.order.first_name == u.first_name and o.order.email == u.email:
            lista.append(o)
    return render(request, 'my_orders.html', {'orders': lista})

def cancel_order(request, id_pedido):
    orders = OrderItem.objects.all()
    for o in orders:
        if o.order.id == id_pedido:
            o.order.delete()
            o.delete()
    return my_orders(request)