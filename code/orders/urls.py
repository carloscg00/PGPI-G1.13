from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('cancel_order/<int:id_pedido>', views.cancel_order, name='cancel_order'),
]