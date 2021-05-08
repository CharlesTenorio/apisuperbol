from django.db.models import TextChoices

class TransactionTypeChoices(TextChoices):
    SHOP_CREDIT = 'sc', 'Comprar creditos'
    WITHDRAW_CREDIT = 'wc',  'Retirar creditos'
    BONUS = 'b', 'Bonus'