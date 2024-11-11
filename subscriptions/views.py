from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import SubscriptionType, Subscription
import stripe

# Create your views here

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def subscription_list(request):
    """View to list all available subscriptions"""
    subscriptions = SubscriptionType.objects.filter(is_active=True)
    
    user_subscriptions = Subscription.objects.filter(user=request.user, is_active=True)
    user_subscription_type_ids = user_subscriptions.values_list('subscription_type_id', flat=True)
    
    context = {
        'subscriptions': subscriptions,
        'user_subscriptions': user_subscriptions,
        'user_subscription_type_ids': list(user_subscription_type_ids),
    }
    return render(request, 'subscriptions/subscription_list.html', context)

@login_required
def subscription_detail(request, subscription_id):
    """View to show subscription details and allow purchase"""
    subscription_type = get_object_or_404(SubscriptionType, id=subscription_id)
    
    context = {
        'subscription': subscription_type,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'subscriptions/subscription_detail.html', context)

@login_required
def create_subscription(request, subscription_id):
    """Handle subscription creation"""
    if request.method == 'POST':
        subscription_type = get_object_or_404(SubscriptionType, id=subscription_id)
        
        try:
            # Create Stripe subscription
            stripe_customer = stripe.Customer.create(
                email=request.user.email,
                source=request.POST['stripeToken']
            )
            
            stripe_subscription = stripe.Subscription.create(
                customer=stripe_customer.id,
                items=[{'price': subscription_type.stripe_price_id}],
            )
            
            # Create local subscription
            subscription = Subscription.objects.create(
                user=request.user,
                subscription_type=subscription_type,
                stripe_subscription_id=stripe_subscription.id,
            )
            
            messages.success(request, f'Successfully subscribed to {subscription_type.name}!')
            return redirect('subscription_list')
            
        except stripe.error.CardError as e:
            messages.error(request, f"Card error: {e.error.message}")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
        
    return redirect('subscription_detail', subscription_id=subscription_id)

@login_required
def manage_subscription(request, subscription_id):
    """View to manage existing subscription"""
    subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'cancel':
            try:
                # Cancel Stripe subscription
                stripe.Subscription.delete(subscription.stripe_subscription_id)
                
                # Update local subscription
                subscription.status = 'CANCELLED'
                subscription.is_active = False
                subscription.save()
                
                messages.success(request, 'Subscription successfully cancelled.')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
    
    context = {
        'subscription': subscription,
    }
    return render(request, 'subscriptions/manage_subscription.html', context)
