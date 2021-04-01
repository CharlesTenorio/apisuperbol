from django.db import models
from django.utils.translation import gettext_lazy as _

class Match(models.Model):
  id = models.CharField(_("Evento id"), max_length=255, primary_key=True, unique=True)
  sport_id	= models.PositiveIntegerField(_("Sport"), default=1)
  league_id = models.ForeignKey("leagues.League", verbose_name=_("Liga"), on_delete=models.CASCADE)
  time = models.CharField(_("Timestemp do jogo"))
  time_status = models.CharField(_("Tempo atual do jogo"), max_length=50, default='0')
  home = models.ForeignKey("teams.Team", verbose_name=_("Casa"), on_delete=models.PROTECT)
  away = models.ForeignKey("teams.Team", verbose_name=_("Fora"), on_delete=models.PROTECT)
  ss = models.CharField(_("Resultado final do jogo"), max_length=50, blank=True, null=True)
  scores = models.JSONField(_("Resultado detalhado"), default={})
  stats = models.JSONField(_("Detalhes da partida"), default={})
  events = models.JSONField(_("Minuto a minuto"), default={})
  extra = models.JSONField(_("Informações adicionais"), default={})

  class Meta:
    verbose_name = _("Partida")
    verbose_name_plural = _("Partidas")

  def __str__(self):
    return f'{self.home.name} x {self.away.name}'

