from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices

class CompanyTypeChoices(IntegerChoices):
  INFORMAL = 0, _('Informal')
  MEI = 1, _('MEI')
  INDIVIDUAL = 2, _('Individual')
  EIRELI = 3, _('Eireli')
  LTDA = 4, _('LTDA')