from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['bill_number', 'customer_name', 'address', 'amount', 
                 'expected_delivery_time', 'payment_mode', 'delivery_agent']
        widgets = {
            'expected_delivery_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AgentOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_mode', 'delivered_at']
        widgets = {
            'delivered_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }