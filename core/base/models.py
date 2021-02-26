from django.db import models
from django.utils.translation import gettext_lazy as _

from core.base.enums.natural import NaturalPersonChoice
from core.base.enums.states import StateChoices
from core.base.fields import CnpjField, ZipCodeField

class AddressMixin(models.Model):
  
  street = models.CharField(_('Rua'), max_length=120)
  street_number = models.CharField(_('Número da casa'), max_length=50, default='sn')
  district = models.CharField(_('Bairro'), max_length=80)
  city = models.CharField(_('Cidade'), max_length=80)
  state = models.CharField(_('Estado'), max_length=2, choices=StateChoices.choices)
  complement = models.CharField(_('Complemento'), max_length=250, blank=True)
  zip_code = ZipCodeField()

  class Meta:
    abstract = True


class PhoneMixin(models.Model):

  phone_prefix = models.CharField(_('DDD'), max_length=2)
  phone_number = models.CharField(_('Telefone'), max_length=9)
    
  def phone(self):
    return f'+55{self.phone_prefix}{self.phone_number}'

  class Meta:
      abstract = True


class PersonDocumentMixin(models.Model):

  is_natural = models.CharField(
    _("Tipo de pessoa"),
    max_length=5,
    choices=NaturalPersonChoice.choices,
    default=NaturalPersonChoice.FISICA
  )
  cpf_cnpj = CnpjField()
  
  class Meta:
    abstract = True

