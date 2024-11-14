from django.test import TestCase
from django.urls import reverse
from .models import Product, Category

# Create your tests here.


class ProductViewsTests(TestCase):

    def setUp(self):
        # Create a test category
        self.category = Category.objects.create(name="Test Category")

        # Create test products
        self.product1 = Product.objects.create(
            name="Test Product 1",
            description="Description of Test Product 1",
            price=10,
            category=self.category
        )
        self.product2 = Product.objects.create(
            name="Test Product 2",
            description="Description of Test Product 2",
            price=20,
            category=self.category
        )

    def test_all_products_view(self):
        """Test that the all products page loads correctly."""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        # Check correct template is used
        self.assertTemplateUsed(response, 'products/products.html')
        # Ensure product 1 is in the response content
        self.assertContains(response, self.product1.name)
        # Ensure product 2 is in the response content
        self.assertContains(response, self.product2.name)

    def test_product_detail_view(self):
        """Test that the product detail page loads correctly."""
        response = self.client.get(
            reverse('product_detail', args=[self.product1.id])
        )
        self.assertEqual(response.status_code, 200)
        # Check correct template is used
        self.assertTemplateUsed(response, 'products/product_detail.html')
        # Ensure the product name appears in the page
        self.assertContains(response, self.product1.name)

    def test_product_search_view(self):
        """Test that the search functionality filters products correctly."""
        response = self.client.get(reverse('products') + '?q=Test Product 1')
        self.assertEqual(response.status_code, 200)
        # Product 1 should be listed
        self.assertContains(response, self.product1.name)
        # Product 2 should not be listed
        self.assertNotContains(response, self.product2.name)
