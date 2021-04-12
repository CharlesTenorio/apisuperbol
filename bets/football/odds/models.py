from django.db import models
from django.utils.translation import gettext_lazy as _

class Odd(models.Model):
  id = models.CharField(_("Evento id"), max_length=255, primary_key=True, unique=True)
  match = models.ForeignKey("match.Match", verbose_name=_("Jogo"), on_delete=models.CASCADE)
  key = models.CharField(_("Market Key"), max_length=50)
  description = models.CharField(_("Descrição"), max_length=150)
  home_od = models.CharField(_("Casa"), max_length=50)
  draw_od = models.CharField(_("Empate"), max_length=50)
  away_od = models.CharField(_("Fora"), max_length=50)
  ss = models.CharField(_("Resultado final do jogo"), max_length=50, blank=True, null=True)
  time_str = models.CharField(_("Tempo atual do jogo"), max_length=50, blank=True, null=True)
  add_time = models.CharField(_("Timestemp do momento da cotação"))

  class Meta:
    verbose_name = _("Cotação")
    verbose_name_plural = _("Cotações")

  def __str__(self):
    return self.description