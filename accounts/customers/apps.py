from django.apps import AppConfig


class CustomersConfig(AppConfig):
    name = 'accounts.customers'
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

    def ready(self):
        import accounts.customers.signals
