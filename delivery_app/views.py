# delivery_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Order, DeliveryAgent
from .forms import OrderForm, AgentOrderUpdateForm
from .utils import get_delivery_analytics

def is_admin(user):
    return user.is_superuser

def is_delivery_agent(user):
    return hasattr(user, 'deliveryagent')

@login_required
def dashboard(request):
    if is_admin(request.user):
        return admin_dashboard(request)
    elif is_delivery_agent(request.user):
        return agent_dashboard(request)
    return redirect('login')

@user_passes_test(is_admin)
def admin_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    agents = DeliveryAgent.objects.all()
    analytics = get_delivery_analytics()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created successfully!')
            return redirect('dashboard')
    else:
        form = OrderForm()
    
    context = {
        'orders': orders,
        'agents': agents,
        'form': form,
        'analytics': analytics,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def agent_dashboard(request):
    if not is_delivery_agent(request.user):
        return redirect('login')
    
    agent = request.user.deliveryagent
    assigned_orders = Order.objects.filter(delivery_agent=agent).order_by('-created_at')
    analytics = get_delivery_analytics(delivery_agent=agent)
    
    context = {
        'orders': assigned_orders,
        'analytics': analytics,
    }
    return render(request, 'agent_dashboard.html', context)

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if is_delivery_agent(request.user) and order.delivery_agent != request.user.deliveryagent:
        messages.error(request, 'You are not authorized to update this order.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        if is_admin(request.user):
            form = OrderForm(request.POST, instance=order)
        else:
            form = AgentOrderUpdateForm(request.POST, instance=order)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully!')
            return redirect('dashboard')
    else:
        if is_admin(request.user):
            form = OrderForm(instance=order)
        else:
            form = AgentOrderUpdateForm(instance=order)
    
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'update_order.html', context)