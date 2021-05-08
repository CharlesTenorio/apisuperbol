from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

from services.bets.bets365.enums.match import TimeStatusChoices as tsc
from services.bets.bets365.enums.sports import SportIDChoices

class Match(models.Model):
  id = models.CharField(_("Evento id"), max_length=255, primary_key=True, unique=True)
  sport_id	= models.CharField(_("Sport"), max_length=50, default=SportIDChoices.Soccer, choices=SportIDChoices.choices)
  league_id = models.ForeignKey("leagues.League", verbose_name=_("Liga"), on_delete=models.CASCADE)
  time = models.CharField(_("Timestemp do jogo"), max_length=200)
  time_status = models.CharField(_("Tempo atual do jogo"), max_length=50, default=tsc.NOT_STARTED, choices=tsc.choices)
  home = models.ForeignKey("teams.Team", verbose_name=_("Casa"), related_name='home_set', on_delete=models.PROTECT)
  away = models.ForeignKey("teams.Team", verbose_name=_("Fora"), related_name='away_set', on_delete=models.PROTECT)
  ss = models.CharField(_("Resultado final do jogo"), max_length=50, blank=True, null=True)
  scores = JSONField(_("Resultado detalhado"), default=dict, blank=True)
  stats = JSONField(_("Detalhes da partida"), default=dict, blank=True)
  events = JSONField(_("Minuto a minuto"), default=dict, blank=True)
  extra = JSONField(_("Informações adicionais"), default=dict, blank=True)

  @property
  def event_date(self):
    return datetime.fromtimestamp(int(self.time)).strftime('%d/%m/%Y ás %H:%M:%S')

  class Meta:
    verbose_name = _("Partida")
    verbose_name_plural = _("Partidas")

  def __str__(self):
    return f'{self.home.name} x {self.away.name}'

