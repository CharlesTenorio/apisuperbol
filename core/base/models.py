from django.db import models
from django.utils.translation import gettext_lazy as _

from core.base.enums.natural import NaturalPersonChoice
from core.base.fields import CnpjField, ZipCodeField, 

class AddressMixin(models.Model):
  
  street = models.CharField(max_length=120)
  street_number = models.CharField(max_length=50)
  district = models.CharField(max_length=80)
  city = models.CharField(max_length=80)
  state = models.CharField(max_length=2)
  complement = models.CharField(max_length=250, blank=True)
  zip_code = ZipCodeField()

  class Meta:
    abstract = True


class PhoneMixin(models.Model):

  phone_prefix = models.CharField(max_length=2)
  phone_number = models.CharField(max_length=9)
    
  def phone(self):
    return f'({self.phone_prefix} {self.phone_number}'

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

