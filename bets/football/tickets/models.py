import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.fields import CpfField
from bets.football.tickets.enums import BetOddTypeChoices


class Ticket(models.Model):
  id = models.UUIDField(_("Identificação"), primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  document = CpfField()
  customer = models.ForeignKey("customer.Customer", verbose_name=_("Cliente"), on_delete=models.CASCADE, blank=True, null=True)
  bench = models.ForeignKey("changers.Changer", verbose_name=_("Cambista"), on_delete=models.CASCADE)
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

  class Meta:
    verbose_name = _("Bilhete")
    verbose_name_plural = _("Bilhetes")

  def __str__(self):
    return self.id


class TicketOddMatch(models.Model):
  ticket = models.ForeignKey(Ticket, verbose_name=_("Cambista"), on_delete=models.CASCADE)
  odd = models.ForeignKey('odds.Odd', verbose_name=_("Cambista"), on_delete=models.CASCADE)1
  bet_in = models.CharField(_("Aposta em"), max_length=50, )



  class Meta:
    verbose_name = _("Ticket")
    verbose_name_plural = _("Tickets")

  def __str__(self):
    return self.id