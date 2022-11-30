from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from . import forms
from cart.forms import CartAddProductForm

preguntas = []

def inicio_view(request):
    return render(request, 'shop/inicio.html')

def sobre_nosotros_view(request):
    return render(request, 'shop/sobre_nosotros.html')


#def atencion_cliente_view(request):
    return render(request, 'shop/atencion_cliente.html')

def cliente_form(request):
    form = forms.clienteForm()
    return render(request, 'shop/atencion_cliente.html', {'form': form})

def reserva_form(request):
    form = forms.reservaForm()
    return render(request, 'shop/reserva_form.html', {'form': form})


def product_list(request, category_slug=None):
        
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    form = forms.buscador_productos(request.GET, initial="")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if form.data:
        p=form.data['producto']
        res = render(request, 'shop/catalogo/product_list.html',{'category': category, 'categories': categories, 'products': products, 'form':form, 'p':p})
    else:
        res = res = render(request, 'shop/catalogo/product_list.html',{'category': category, 'categories': categories, 'products': products, 'form':form})
    return res


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/catalogo/detail.html', {'product': product,
                                    'cart_product_form': cart_product_form})