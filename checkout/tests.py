from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from django.urls import reverse

class CheckoutTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a product for the bag (no stock field included)
        self.product = Product.objects.create(
            name='Test Product',
            price=100,  # Price for the product
            description='A test product.',
        )

    def test_checkout_page_get(self):
        """Test if the checkout page loads correctly."""
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Add a product to the session bag (shopping cart)
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()  # Save the session data

        # Get the checkout page
        response = self.client.get(reverse('checkout'))  # Adjusted to use reverse


    def test_checkout_page_get_empty_bag(self):
        """Test if the user is redirected when the cart is empty."""
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Ensure the cart is empty
        self.client.session['bag'] = {}
        self.client.session.save()

        # Get the checkout page
        response = self.client.get(reverse('checkout'))  # Adjusted to use reverse


    def test_checkout_post_valid(self):
        """Test if POST request with valid data leads to a successful redirect."""
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Add a product to the session bag
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()

        # POST valid data to the checkout page
        response = self.client.post(reverse('checkout'), {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'country': 'USA',
            'postcode': '12345',
            'town_or_city': 'Test Town',
            'street_address1': '123 Test Street',
            'street_address2': 'Apt 4B',
            'county': 'Test County',
            'client_secret': 'test_secret_123',
        })

        # Check that the user is redirected after successful form submission
        self.assertEqual(response.status_code, 302)

        # Since the redirect URL contains the order number, we check if it starts with /checkout/checkout_success/
        self.assertTrue(response.url.startswith('/checkout/checkout_success/'))
