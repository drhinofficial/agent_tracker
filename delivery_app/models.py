from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class DeliveryAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return self.user.get_full_name()

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('UPI', 'UPI'),
    ]
    
    bill_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expected_delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField(null=True, blank=True)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.bill_number} - {self.customer_name}"