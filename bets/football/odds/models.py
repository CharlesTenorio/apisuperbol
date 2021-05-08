from django.db import models
from django.utils.translation import gettext_lazy as _

from services.bets.bets365.enums.odds import OddMarketsChoices, OddTypeChoices

# https://betsapi.com/docs/events/odds.html


class Odd(models.Model):
  id = models.CharField(_("id"), max_length=255, primary_key=True, unique=True)
  event_id = models.CharField(_("Evento id"), max_length=255)
  match = models.ForeignKey("match.Match", verbose_name=_("Jogo"), on_delete=models.CASCADE)
  market = models.CharField(_("Market Key"), max_length=50, choices=OddMarketsChoices.choices)
  source = models.CharField(_("Api name"), max_length=50, default='bet365')
  description = models.CharField(_("Descrição"), max_length=150, null=True, blank=True)
  
  first_od = models.CharField(_("Label 1"), max_length=50, choices=OddTypeChoices.choices)
  first_od_value = models.CharField(_("Valor 1"), max_length=50)
  second_od = models.CharField(_("Label 2"), max_length=50, choices=OddTypeChoices.choices)
  second_od_value = models.CharField(_("Valor 2"), max_length=50)
  last_od = models.CharField(_("Label 3"), max_length=50)
  last_od_value = models.CharField(_("Valor 3"), max_length=50, choices=OddTypeChoices.choices)
  
  ss = models.CharField(_("Resultado final do jogo"), max_length=50, blank=True, null=True)
  time_str = models.CharField(_("Tempo atual do jogo"), max_length=50, blank=True, null=True)
  add_time = models.CharField(_("Timestemp do momento da cotação"), max_length=100)

  class Meta:
    verbose_name = _("Cotação")
    verbose_name_plural = _("Cotações")

  def __str__(self):
    return self.description