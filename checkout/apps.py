from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Import signals to ensure they are loaded and connected.
        """
        import checkout.signals  # registers the signals

