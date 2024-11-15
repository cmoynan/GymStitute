from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order/<order_number>/', views.order_detail, name='order_detail'),
]
