from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DeliveryAgent, Order

@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'customer_name', 'amount', 'delivery_agent', 
                   'expected_delivery_time', 'delivered_at', 'payment_mode')
    list_filter = ('payment_mode', 'delivery_agent', 'delivered_at')
    search_fields = ('bill_number', 'customer_name', 'address')
    date_hierarchy = 'created_at'