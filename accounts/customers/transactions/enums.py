from django.db.models import TextChoices

class TransactionTypeChoices(TextChoices):
    ('Compra creditos', 'Comprar creditos'),
    ('Retirar creditos', 'Retirar creditos'),
    ('Bonuns', 'Bonuns'),