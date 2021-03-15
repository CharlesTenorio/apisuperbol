from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'accounts.users'
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'

    def ready(self):
        import accounts.users.signals
