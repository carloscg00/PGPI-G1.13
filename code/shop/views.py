from django.shortcuts import render
from django.http import HttpResponse
from . import forms

preguntas = []

def inicio_view(request):
    return render(request, 'myshop/inicio.html')

def sobre_nosotros_view(request):
    return render(request, 'myshop/sobre_nosotros.html')

def catalogo_view(request):
    return render(request, 'myshop/catalogo.html')

def atencion_cliente_view(request):
    if len(preguntas)==0:
        res = render(request, 'myshop/atencion_cliente.html')
    else:
        res = render(request, 'myshop/atencion_cliente.html',{'preguntas':preguntas})
    return res

def atencion_cliente_datos(request):
    if request.method=="GET":    
        tipo = request.GET['tipo']
        cuestion = request.GET['cuestion']
        tupla = (tipo,cuestion)
        preguntas.append(tupla)
    context = {'preguntas':preguntas}
    return render(request, 'myshop/atencion_cliente.html',context)

def cliente_form(request):
    form = forms.clienteForm()
    return render(request, 'myshop/atencion_cliente.html', {'form': form})
