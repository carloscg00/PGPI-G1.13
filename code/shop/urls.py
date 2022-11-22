from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('inicio', views.inicio_view, name="inicio"),
    path('sobre_nosotros', views.sobre_nosotros_view, name="sobre_nosotros"),
    path('catalogo', views.catalogo_view, name="catalogo"),
    path('atencion_cliente', views.atencion_cliente_view, name="atencion_cliente"),
    path('atencion_cliente_datos',views.atencion_cliente_datos, name="atencion_cliente_datos"),
    path('account/', include('account.urls'), name='login'),
    path('account/', include('account.urls'), name='register'),
]