from django.apps import AppConfig


class OwnersConfig(AppConfig):
    name = 'accounts.owners'
    verbose_name = 'Proprietario'
    verbose_name_plural = 'ClieProprietariontes'

    def ready(self):
        import accounts.owners.signals

