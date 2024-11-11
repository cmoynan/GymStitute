from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class SubscriptionType(models.Model):
    """Model for different types of subscriptions available"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    stripe_price_id = models.CharField(max_length=100, blank=True, null=True)
    
    SUBSCRIPTION_CHOICES = [
        ('WORKOUT', 'Personalized Workout Plan'),
        ('MEAL', 'Meal Plan Subscription'),
    ]
    
    subscription_type = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_CHOICES,
        default='WORKOUT'
    )
    
    features = models.JSONField(default=list)  # Store list of features
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_subscription_type_display()} - £{self.price}/month"
    
    class Meta:
        verbose_name_plural = "Subscription Types"

class Subscription(models.Model):
    """Model for user subscriptions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stripe_subscription_id = models.CharField(max_length=100, blank=True, null=True)
    next_billing_date = models.DateTimeField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('CANCELLED', 'Cancelled'),
        ('PAST_DUE', 'Past Due'),
        ('UNPAID', 'Unpaid'),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.subscription_type.get_subscription_type_display()}"
    
    class Meta:
        unique_together = ['user', 'subscription_type']  # User can't have duplicate subscription types

class SubscriptionBenefit(models.Model):
    """Model for tracking subscription benefits used"""
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='benefits_used')
    benefit_name = models.CharField(max_length=200)
    date_used = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.subscription.user.username} used {self.benefit_name}"