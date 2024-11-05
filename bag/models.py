from django.db import models
from products.models import Product
from django.conf import settings

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} - {self.full_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} on order {self.order.id}'

