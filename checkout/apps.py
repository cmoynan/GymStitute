from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Import signals to ensure they are loaded and connected.
        """
        import checkout.signals  # registers the signals
