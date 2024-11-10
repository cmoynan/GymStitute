from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'products']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class ProfileSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return ['profile']

    def location(self, item):
        return reverse(item)
