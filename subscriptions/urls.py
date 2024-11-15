from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path(
        '<int:subscription_id>/',
        views.subscription_detail, name='subscription_detail'
    ),
    path(
        'create/<int:subscription_id>/',
        views.create_subscription, name='create_subscription'
    ),
    path(
        'manage/<int:subscription_id>/',
        views.manage_subscription, name='manage_subscription'
    ),
]
