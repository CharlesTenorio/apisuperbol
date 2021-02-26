from django.db import models
from django.utils.translation import gettext_lazy as _

class Brand(models.Model):
  name = models.CharField(_("Nome"), max_length=80)
  description = models.CharField(_("Descrição"), max_length=50)
  is_active = models.BooleanField(_("Ativa?"), default=True)

  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'