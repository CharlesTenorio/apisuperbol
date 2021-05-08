from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from requests import NullHandler
from core.base.enums.general import YesNoChoices

from services.bets.bets365.enums.countries import CountryChoices
from services.bets.bets365.enums.sports import SportIDChoices

class League(models.Model):
  id = models.CharField(_("Id"), max_length=50, primary_key=True, unique=True)
  sport_id = models.CharField(_("Sport"), max_length=4, default=SportIDChoices.Soccer, choices=SportIDChoices.choices)
  name = models.CharField(_("Nome"), max_length=250)
  cc = models.CharField(_("País"), max_length=4, choices=CountryChoices.choices, blank=True, null=True)
  has_leaguetable = models.SmallIntegerField(
    _("Tem tabela de classificação?"),
    choices=YesNoChoices.choices,
    default=0
  )
  has_toplist =  models.SmallIntegerField(
    _("Tem lista principal?"),
    choices=YesNoChoices.choices,
    default=0
  )

  class Meta:
    ordering = ['name', ]
    verbose_name = _("League")
    verbose_name_plural = _("Leagues")

  def __str__(self):
    return self.name
