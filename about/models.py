from django.db import models

# Create your models here.
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)  # Make sure emails are unique
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
