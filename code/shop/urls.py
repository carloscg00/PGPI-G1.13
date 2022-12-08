from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('sobre_nosotros', views.sobre_nosotros_view, name='sobre_nosotros'),
    path('atencion_cliente', views.cliente_form, name='atencion_cliente'),
    path('buscador', views.buscador, name='buscador'),
    path('account/', include('account.urls'), name='login'),
    path('account/', include('account.urls'), name='register'),
    path('orders/', include('orders.urls'), name='orders'),
    path('reserva_form/',views.reserva_form, name='reserva_form'),
    path('product_list', views.product_list, name='product_list'),
    path('product_list/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product_list/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]   