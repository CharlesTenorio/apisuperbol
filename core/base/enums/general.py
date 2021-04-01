from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class YesNoChoices(IntegerChoices):
  YES = 1, _('Sim')
  NO = 0, _('Não')