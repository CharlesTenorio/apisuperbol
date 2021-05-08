import uuid
from decimal import Decimal
from django.db import models
from django.db.models.aggregates import Sum
from django.utils.translation import gettext_lazy as _

from core.base.fields import CpfField
from services.bets.bets365.enums.odds import OddTypeChoices


class Ticket(models.Model):
  id = models.UUIDField(_("Identificação"), primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  bench = models.ForeignKey("changers.Changer", verbose_name=_("Cambista"), on_delete=models.CASCADE)
  customer = models.ForeignKey("customers.Customer", verbose_name=_("Cliente"), on_delete=models.CASCADE, blank=True, null=True)
  document = CpfField(verbose_name=_('Documento'))
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)


  @property
  def total(self):
    result = self.ticketbets.all().aggregates(total=Sum('bet_amount'))
    return result['total'] or Decimal(0)

  @property
  def total_win(self):
    result = self.ticketbets.filter(is_checked=True, is_win=True).aggregates(total=Sum('bet_amount'))
    return result['total'] or Decimal(0)

  @property
  def count_bets(self):
    return self.ticketbets.all().count()

  @property
  def count_win_bets(self):
    return self.ticketbets.filter(is_checked=True, is_win=True).count()
  
  @property
  def count_lose_bets(self):
    return self.ticketbets.filter(is_checked=True, is_win=False).count()
    

  class Meta:
    verbose_name = _("Bilhete")
    verbose_name_plural = _("Bilhetes")

  def __str__(self):
    return self.id


class TicketOddMatch(models.Model):
  ticket = models.ForeignKey(Ticket, verbose_name=_("Bilhete"), related_name='ticketbets', on_delete=models.CASCADE)
  odd = models.ForeignKey('odds.Odd', verbose_name=_("Cotação"), on_delete=models.CASCADE)
  bet_value = models.CharField(_("Palpite do jogo"), max_length=50)
  bet_amount = models.DecimalField(_("valor da aposta"), max_digits=5, decimal_places=2)
  bet_chances = models.DecimalField(_("Valor da cotação"), max_digits=5, decimal_places=2)
  is_checked = models.BooleanField(_("foi Verificado?"), default=False)
  is_win = models.BooleanField(_("Ganhou?"), default=False)
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)


  class Meta:
    verbose_name = _("Aposta")
    verbose_name_plural = _("Aposta")

  def __str__(self):
    return self.id