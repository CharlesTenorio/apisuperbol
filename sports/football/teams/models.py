from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.enums.general import YesNoChoices

class Team(models.Model):
  id = models.CharField(_("Id"), max_length=50, primary_key=True, unique=True)
  name = models.CharField(_("Nome"), max_length=250)
  cc = models.CharField(_("Continente"), max_length=150)
  image_id =  models.CharField(_("Escudo do time"))
  has_squad = models.SmallIntegerField(
    _("Tem esquadrão?"),
    choices=YesNoChoices.choices,
    default=0
  )

  class Meta:
    verbose_name = _("Time")
    verbose_name_plural = _("Times")

    def __str__(self):
      return self.name
