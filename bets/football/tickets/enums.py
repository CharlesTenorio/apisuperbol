from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BetOddTypeChoices(TextChoices):
  HOME = 'home_od', _('Casa')
  DRAW = 'draw_od', _('Empate')
  AWAY = 'away_od', _('Fora')
  OVER = 'over_od', _('Vê com zé')
  HANDICAP = 'handicap', _('Escanteios')
  UNDER = 'under_od', _('Não sei')
