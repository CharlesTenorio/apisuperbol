from datetime import datetime

from services.bets.bets365.enums.match import TimeStatusChoices
from services.bets.bets365.enums.sports import SportIDChoices

from sports.football.match.models import Match
from sports.football.leagues.tools import get_or_create_league
from sports.football.teams.tools import get_or_create_team


def get_or_create_match(event:dict) -> Match:
  if match := get_and_update_match(event):
    return match

  return get_and_create_match(event)
  


def get_and_create_match(event:dict):
  league = get_or_create_league(event)
  home = get_or_create_team(team=event['home'])
  away = get_or_create_team(team=event['away'])

  return Match.objects.create(
    league_id = league,
    home = home,
    away = away,
    id = event['id'],
    sport_id	= event.get('sport_id', SportIDChoices.Soccer),
    time = event.get('time', str(datetime.now().timestamp())),
    time_status = event.get('time_status', TimeStatusChoices.NOT_STARTED),
    ss = event.get('ss', None),
    extra = event.get('extra', {}),
    scores = event.get('scores', {}),
    stats = event.get('stats', {}),
    events = event.get('events', {}),
  )

def get_and_update_match(event:dict):
  qs = Match.objects.filter(id=event['id'])
  if qs.exists():
    league = get_or_create_league(event)
    home = get_or_create_team(team=event['home'])
    away = get_or_create_team(team=event['away'])
    qs.update(
      league_id = league,
      home = home,
      away = away,
      sport_id	= event.get('sport_id', SportIDChoices.Soccer),
      time = event.get('time', str(datetime.now().timestamp())),
      time_status = event.get('time_status', TimeStatusChoices.NOT_STARTED),
      ss = event.get('ss', None),
      extra = event.get('extra', {}),
      scores = event.get('scores', {}),
      stats = event.get('stats', {}),
      events = event.get('events', {}),
    )
    return qs.first()