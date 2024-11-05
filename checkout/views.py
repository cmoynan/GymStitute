from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from .models import Order, OrderItem
from products.models import Product

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == 'POST':
        # Collect order details from POST data
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        country = request.POST['country']

        # Calculate order total
        bag = request.session.get('bag', {})
        total = sum(Product.objects.get(id=item_id).price * quantity for item_id, quantity in bag.items())

        # Create an Order object
        order = Order.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country,
            total=total
        )

        # Create OrderItems and attach to the order
        for item_id, quantity in bag.items():
            product = Product.objects.get(id=item_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                item_total=product.price * quantity
            )

        # Create Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(total * 100),  # Stripe expects cents
            currency='usd',
            metadata={'order_id': order.id}
        )

        # Pass data to the template
        return render(request, 'checkout/checkout.html', {
            'order': order,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret
        })
    
    return render(request, 'checkout/checkout.html')