from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import SubscriptionType, Subscription
import stripe
from django.conf import settings

# Mock the Stripe API key for testing
stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriptionViewsTests(TestCase):

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )
        self.client.login(username='testuser', password='password123')

        # Create test subscription types with required fields (including price)
        self.subscription_type = SubscriptionType.objects.create(
            name="Basic Plan", 
            description="Description of Basic Plan", 
            stripe_price_id="price_test", 
            price=10.00,  # Add the missing price field here
            is_active=True
        )

        # Create a subscription for the user
        self.subscription = Subscription.objects.create(
            user=self.user, 
            subscription_type=self.subscription_type, 
            stripe_subscription_id="sub_test", 
            is_active=True
        )

    def test_subscription_list_view(self):
        """Test that the subscription list page loads correctly"""
        response = self.client.get(reverse('subscription_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'subscriptions/subscription_list.html'
        )  # Correct template used
        self.assertContains(
            response, self.subscription_type.name
        )  # Ensure the subscription type is in the response

    def test_subscription_detail_view(self):
        """Test that the subscription detail page loads correctly"""
        response = self.client.get(
            reverse('subscription_detail', args=[self.subscription_type.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'subscriptions/subscription_detail.html'
        )  # Correct template used
        self.assertContains(
            response, self.subscription_type.name
        )  # Ensure the subscription name is in the response

    def test_create_subscription_view(self):
        """Test that creating a new subscription works"""
        # Create a mock POST request to simulate subscribing
        post_data = {
            'stripeToken': 'tok_visa',  # Mock Stripe token for testing
        }
        response = self.client.post(
            reverse('create_subscription', args=[self.subscription_type.id]),
            post_data
        )
        self.assertEqual(
            Subscription.objects.latest('id').user, self.user
        )  # Ensure the subscription belongs to the logged-in user
