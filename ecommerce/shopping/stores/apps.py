from django.apps import AppConfig


class StoresConfig(AppConfig):
    name = 'ecommerce.shopping.stores'
    verbose_name = 'Vendas'

    def ready(self):
        import ecommerce.shopping.stores.signals
