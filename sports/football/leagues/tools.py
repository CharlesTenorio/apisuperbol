from sports.football.leagues.models import League


def get_or_create_league(event:dict):
  league:dict = event['league']
  league, _ = League.objects.get_or_create(
    id = league['id'],
    name = league['name'],
    cc = league['cc'],
    sport_id = event['sport_id']
  )
  return league