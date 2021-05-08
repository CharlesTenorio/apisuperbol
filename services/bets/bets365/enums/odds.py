from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class OddTypeChoices(TextChoices):
  HOME = 'home_od', _('Casa')
  DRAW = 'draw_od', _('Empate')
  AWAY = 'away_od', _('Fora')
  OVER = 'over_od', _('Vê com zé')
  HANDICAP = 'handicap', _('Escanteios')
  UNDER = 'under_od', _('Não sei')


class OddMarketsChoices(TextChoices):

  FULL_TIME_RESULT = '1_1	', ' 1X2, Full Time Result'
  ASIAN_HANDICAP = '1_2	', ' Asian Handicap'
  GOAL_LINE = '1_3	', ' O/U, Goal Line'
  ASIAN_CORNERS = '1_4	', ' Asian Corners'
  FIRST_HALF_ASIAN_HANDICAP = '1_5	', ' 1st Half Asian Handicap'
  FIRST_HALF_GOAL_LINE = '1_6	', ' 1st Half Goal Line'
  FIRST_HALF_ASIAN_CORNERS = '1_7	', ' 1st Half Asian Corners	1_8	Half Time Result'
  MONEY_LINE = '18_1',	'Money Line'
  SPREAD = '18_2',	'Spread'
  TOAL_POINTS = '18_3',	'Total Points'
  MONEY_LINE_HALF = '18_4',	'Money Line (Half)'
  SPREAD_HALF = '18_5',	'Spread (Half)'
  TOTAL_POINTS_HALF = '18_6',	'Total Points (Half)'
  QUARTER_WINNER_2_WAY = '18_7',	'Quarter - Winner (2-Way)'
  QUARTER_HANDICAP = '18_8',	'Quarter - Handicap'
  QUARTER_TOTAL_2_WAY = '18_9',	'Quarter - Total (2-Way)'
  MATCH_WINNER_2_WAY = '*_1	', ' Match Winner 2-Way'
  ASIAN_HANDICAP_2  = '*_2	', ' Asian Handicap'
  OVER_UNDER = '*_3	', ' Over/Under'
  DRAW_NO_BET = '3_4	', ' Draw No Bet (Cricket)'
