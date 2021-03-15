from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices, TextChoices

class CompanyTypeChoices(IntegerChoices):
  INFORMAL = 0, _('Informal')
  MEI = 1, _('MEI')
  INDIVIDUAL = 2, _('Individual')
  EIRELI = 3, _('Eireli')
  LTDA = 4, _('LTDA')


class NaturalPersonChoice(TextChoices):
  FISICA = 'CPF', _('Pessoa Física')
  JURIDICA = 'CNPJ', _('Pessoa Jurídica')


class SexPersonChoice(TextChoices):
  Male = 'm', _('Masculino')
  Female = 'f', _('Feminino')

