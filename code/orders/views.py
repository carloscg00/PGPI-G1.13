from django.urls import reverse
from django.shortcuts import render, get_object_or_404
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
    orderItems = OrderItem.objects.all()
    orders = Order.objects.all()
    lista = []
    u = request.user
    for o in orders:
        if o.first_name == u.first_name and o.email == u.email:
            lista.append(o)
    return render(request, 'my_orders.html', {'orderItems': orderItems, 'orders': lista})

def cancel_order(request, id_pedido):
    orders = Order.objects.all()
    orderItems = OrderItem.objects.all()
    for o in orders:
        if o.id == id_pedido:
            o.delete()
            for i in orderItems:
                if i.order == o:
                    i.delete()
    return my_orders(request)