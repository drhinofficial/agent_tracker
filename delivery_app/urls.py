from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),
]