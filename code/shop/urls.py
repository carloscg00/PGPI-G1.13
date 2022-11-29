from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('sobre_nosotros', views.sobre_nosotros_view, name='sobre_nosotros'),
    path('atencion_cliente', views.atencion_cliente_view, name='atencion_cliente'),
    path('atencion_cliente_datos',views.atencion_cliente_datos, name='atencion_cliente_datos'),
    path('account/', include('account.urls'), name='login'),
    path('account/', include('account.urls'), name='register'),
    path('reserva_form/',views.reserva_form, name='reserva_form'),
    path('product_list', views.product_list, name='product_list'),
    path('product_list/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product_list/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]   