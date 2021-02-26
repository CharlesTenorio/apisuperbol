from django.apps import AppConfig


class SalesConfig(AppConfig):
    name = 'ecommerce.shopping.sales'
    verbose_name = 'Vendas'

    def ready(self):
        import ecommerce.shopping.sales.signals