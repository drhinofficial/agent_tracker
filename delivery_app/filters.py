import django_filters
from .models import Order
from django import forms

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='gte',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_date = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='lte',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    class Meta:
        model = Order
        fields = {
            'bill_number': ['icontains'],
            'customer_name': ['icontains'],
            'delivery_agent': ['exact'],
            'payment_mode': ['exact'],
            'delivered_at': ['isnull'],
        }