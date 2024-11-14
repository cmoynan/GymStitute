from django.test import TestCase, Client
from django.urls import reverse


class BagViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')
        self.add_to_bag_url = reverse('add_to_bag', args=['test_item'])
        self.remove_from_bag_url = reverse('remove_from_bag', args=['test_item'])

    def test_view_bag_template(self):
        """Test that the bag page renders the correct template."""
        response = self.client.get(self.view_bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_without_size(self):
        """Test adding a product without a size to the shopping bag."""
        response = self.client.post(self.add_to_bag_url, {
            'quantity': 2,
            'redirect_url': self.view_bag_url,
        })
        # Check for redirect
        self.assertEqual(response.status_code, 302)
        bag = self.client.session.get('bag', {})
        # Check item is added
        self.assertIn('test_item', bag)
        # Check correct quantity added
        self.assertEqual(bag['test_item'], 2)
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any(
            '2 of the product added to your bag!' in str(message)
            for message in messages
        ))

    def test_add_to_bag_with_size(self):
        """Test adding a product with a size to the shopping bag."""
        response = self.client.post(self.add_to_bag_url, {
            'quantity': 1,
            'product_size': 'M',
            'redirect_url': self.view_bag_url,
        })
        self.assertEqual(response.status_code, 302)
        bag = self.client.session.get('bag', {})
        self.assertIn('test_item', bag)
        self.assertIn('M', bag['test_item']['items_by_size'])  # Check size 'M' added
        self.assertEqual(bag['test_item']['items_by_size']['M'], 1)
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any(
            '1 x M added to your bag!' in str(message)
            for message in messages
        ))

    def test_remove_from_bag(self):
        """Test removing a product from the shopping bag."""
        # Add item to the bag first
        session = self.client.session
        session['bag'] = {'test_item': 2}
        session.save()

        response = self.client.post(self.remove_from_bag_url)
        self.assertEqual(response.status_code, 302)
        bag = self.client.session.get('bag', {})
        self.assertNotIn('test_item', bag)  # Item should be removed
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any(
            'Item successfully removed from your bag!' in str(message)
            for message in messages
        ))

    def test_remove_nonexistent_item(self):
        """Test removing an item that doesn't exist in the bag."""
        response = self.client.post(self.remove_from_bag_url)
        self.assertEqual(response.status_code, 302)
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any(
            'Item not found in your bag.' in str(message)
            for message in messages
        ))
