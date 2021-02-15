from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class PaymentGatewayChoices(TextChoices):
  CIELO = 'cielo', 'Cielo'
  MERCADO_PAGO = 'mercadopago', 'Mercado Pago'
  PAYPAL = 'paypal', 'PayPal'
  IUGU = 'iugu', 'Iugu'
  PAGARME = 'pagarme', 'Pagar.me'


class PaymentTypeChoices(TextChoices):
  CREDIT_CARD = 'credit_card', _('Cartão de crédito')
  BANK_SLIP = 'bank_slip', _('Boleto')
  PIX = 'pix', _('Pix')


class PaymentStatusChoices(TextChoices):
  PENDING = 'pending', _('Pendente')
  PAID = 'paid', _('Pago')
  CANCELED = 'canceled', _('Cancelado')
  RESUFED = 'refused', _('Recusado')
  EXPIRED = 'expired', _('Expirado')
  REFUNDED = 'refunded', _('Reembolsado')
  CHARGEBACK = 'chargeback', _('Chargeback')
  IN_PROTEST = 'in_protest', _('Contestada')