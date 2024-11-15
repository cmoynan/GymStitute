from django.contrib import admin
from .models import SubscriptionType, Subscription, SubscriptionBenefit


@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscription_type', 'price', 'is_active')
    list_filter = ('subscription_type', 'is_active')
    search_fields = ('name', 'description')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_type', 'status',
                    'start_date', 'next_billing_date')

    list_filter = ('status', 'is_active', 'subscription_type')
    search_fields = ('user__username', 'user__email', 'stripe_subscription_id')
    date_hierarchy = 'start_date'


@admin.register(SubscriptionBenefit)
class SubscriptionBenefitAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'benefit_name', 'date_used', 'value')
    list_filter = ('benefit_name', 'date_used')
    search_fields = ('subscription__user__username', 'benefit_name')
    date_hierarchy = 'date_used'
