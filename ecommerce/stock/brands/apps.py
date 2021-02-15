from django.apps import AppConfig


class BrandsConfig(AppConfig):
    name = 'ecommerce.stock.brands'
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'

    def ready(self):
        import ecommerce.stock.brands.signals
