from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from . import forms

preguntas = []

def inicio_view(request):
    return render(request, 'shop/inicio.html')

def sobre_nosotros_view(request):
    return render(request, 'shop/sobre_nosotros.html')


def atencion_cliente_view(request):
    if len(preguntas)==0:
        res = render(request, 'shop/atencion_cliente.html')
    else:
        res = render(request, 'shop/atencion_cliente.html',{'preguntas':preguntas})
    return res

def atencion_cliente_datos(request):
    if request.method=="GET":    
        tipo = request.GET['tipo']
        cuestion = request.GET['cuestion']
        tupla = (tipo,cuestion)
        preguntas.append(tupla)
    context = {'preguntas':preguntas}
    return render(request, 'shop/atencion_cliente.html',context)

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
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/catalogo/product_list.html',{'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/catalogo/detail.html', {'product': product})