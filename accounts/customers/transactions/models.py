import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Account(models.Model):
    id = models.UUIDField(_("Identificação"), primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer = models.OneToOneField("customers.Customer", verbose_name=_("Apostador"), on_delete=models.PROTECT)
    balance = models.DecimalField(_("Saldo em conta"), max_digits=9, decimal_places=2)
    bonus = models.DecimalField(_("Bonus em conta"), max_digits=9, decimal_places=2)

    @property
    def total(self):
      return self.balance + self.bonus
    
    def __str__(self):
      return self.customer

    class Meta:
        db_table = 'conta'
        managed = True
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Transaction(models.Model):
    id = models.UUIDField(_("Identificação"), primary_key=True, default=uuid.uuid5, editable=False, unique=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name=_("Conta"))
    movimentacao = models.CharField(max_length=20, choices=settings.TIPO_MOVIMENTACAO)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    movi_data = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return self.movimentacao

    class Meta:
        db_table = 'historicoconta'
        managed = True
        verbose_name = 'historico'
        verbose_name_plural = 'historicos'