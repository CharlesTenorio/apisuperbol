from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'ecommerce.stock.products'
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'

    def ready(self):
        import ecommerce.stock.products.signals
