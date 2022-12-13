from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'paid', 'book_date',
        'confirmed', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'book_date', 'confirmed']
    list_editable = ['paid', 'confirmed']
    inlines = [OrderItemInline]