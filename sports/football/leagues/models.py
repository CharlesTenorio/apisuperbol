from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.enums.general import YesNoChoices

class League(models.Model):
  id = models.CharField(_("Id"), max_length=50, primary_key=True, unique=True)
  name = models.CharField(_("Nome"), max_length=250)
  cc = models.CharField(_("Continente"), max_length=150)
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
    verbose_name = _("League")
    verbose_name_plural = _("Leagues")

  def __str__(self):
    return self.name
