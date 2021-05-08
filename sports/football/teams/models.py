from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.enums.general import YesNoChoices

from services.bets.bets365.enums.countries import CountryChoices

class Team(models.Model):
  id = models.CharField(_("Id"), max_length=50, primary_key=True, unique=True)
  name = models.CharField(_("Nome"), max_length=250)
  cc = models.CharField(_("País"), max_length=4, choices=CountryChoices.choices, blank=True, null=True)
  image_id =  models.CharField(_("Escudo do time"), max_length=100, blank=True, null=True)
  has_squad = models.SmallIntegerField(
    _("Tem esquadrão?"),
    choices=YesNoChoices.choices,
    default=0
  )

  @property
  def assets_url(self):
    return 'https://assets.b365api.com/images/team'

  @property
  def image_small(self):
    if self.image_id:
      return f'{self.assets_url}/s/{self.image_id}.png'
    return None
  
  @property
  def image_medium(self):
    if self.image_id:
      return f'{self.assets_url}/m/{self.image_id}.png'
    return None
  
  @property
  def image_big(self):
    if self.image_id:
      return f'{self.assets_url}/b/{self.image_id}.png'
    return None

  def __str__(self):
    return self.name
  class Meta:
    verbose_name = _("Time")
    verbose_name_plural = _("Times")

    def __str__(self):
      return self.name
