from django.db.models import Count, Avg, Sum
from django.utils import timezone
from datetime import timedelta

def get_delivery_analytics(delivery_agent=None):
    from .models import Order
    
    queryset = Order.objects
    if delivery_agent:
        queryset = queryset.filter(delivery_agent=delivery_agent)
    
    now = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = today_start - timedelta(days=7)
    month_ago = today_start - timedelta(days=30)
    
    analytics = {
        'total_orders': queryset.count(),
        'delivered_orders': queryset.filter(delivered_at__isnull=False).count(),
        'pending_orders': queryset.filter(delivered_at__isnull=True).count(),
        
        'today_orders': queryset.filter(created_at__gte=today_start).count(),
        'today_delivered': queryset.filter(delivered_at__gte=today_start).count(),
        
        'weekly_orders': queryset.filter(created_at__gte=week_ago).count(),
        'weekly_delivered': queryset.filter(delivered_at__gte=week_ago).count(),
        
        'monthly_orders': queryset.filter(created_at__gte=month_ago).count(),
        'monthly_delivered': queryset.filter(delivered_at__gte=month_ago).count(),
        
        'payment_distribution': list(queryset.values('payment_mode').annotate(
            count=Count('id')
        )),
        
        'total_revenue': queryset.aggregate(Sum('amount'))['amount__sum'] or 0,
    }
    
    return analytics