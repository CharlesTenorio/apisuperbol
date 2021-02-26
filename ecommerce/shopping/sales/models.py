import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
# from django.contrib.postgres.fields import ArrayField

from core.base.enums.payments import PaymentGatewayChoices, PaymentStatusChoices, PaymentTypeChoices


class Sale(models.Model):
  order = models.UUIDField(_('Código da venda'), default=uuid.uuid4, editable=False, unique=True)
  customer = models.ForeignKey("customers.Customer", verbose_name=_("Cliente"), on_delete=models.PROTECT)
  gateway = models.CharField(_('Gateway'), max_length=50, choices=PaymentGatewayChoices.choices)
  # coupon = models.ForeignKey('discounts.Coupon', on_delete=models.SET_NULL, verbose_name='Cupom', null=True, blank=True)
  invoice_id = models.CharField(max_length=250)
  installments = models.PositiveSmallIntegerField(default=1)
  pay_type = models.CharField(
    _("Tipo de pagamento"), 
    max_length=50,
    choices=PaymentTypeChoices.choices
  )
  pay_status = models.CharField(
    _("Situação do pagamento"), 
    max_length=50,
    choices=PaymentStatusChoices.choices,
    default=PaymentStatusChoices.PENDING
  )
  is_verificated = models.BooleanField(_("Verificado"), default=False)
  paid_at = models.DateTimeField(verbose_name='Pago em', null=True, blank=True)
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

  @property
  def discount(self):
    if self.coupon:
      return Decimal(self.amount * self.coupon.percent)
    return Decimal(0)

  @property
  def items(self):
    return self.saleitem_set.all()

  @property
  def amount(self):
    qs = self.items.annotate(
      price_item=models.F('product__retail_price') * models.F('quantity')
    ).agreggate(amount=models.Sum('price_item'))
    return Decimal(qs.get('amount', 0))

  @property
  def total(self):
    return self.amount - self.discount

  @property
  def total_cents(self):
    return self.total * Decimal(100)


class SaleItem(models.Model):
  sale = models.ForeignKey(Sale, verbose_name=_("Pedido"), on_delete=models.PROTECT)
  product = models.ForeignKey("products.Product", verbose_name=_("Produto"), on_delete=models.PROTECT)
  quantity = models.PositiveSmallIntegerField(_("Quantidade"))
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

  @property
  def amount(self):
    return self.product.retail_price * self.quantity