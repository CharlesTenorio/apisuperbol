from datetime import date
import requests
from django.conf import settings
from core.interfaces.Ibet import IBetsAPI

class Bets365API(IBetsAPI):

  BASE_URL = 'https://api.b365api.com'

  def __init__(self):
    self.TOKEN_API = settings.BETS365_TOKEN
    super().__init__()

  def get_today_to_api(self):
    # format YYYYMMDD, eg: 20161201
    day = date.today().day
    month = date.today().month
    if month < 10:
      month = f'0{month}'
    year = date.today().year
    return f'{year}{month}{day}'

  def request_api(self, url:str, params:dict={}):
    params["token"] = self.TOKEN_API
    resp = requests.get(f'{self.BASE_URL}{url}', params=params)
    print(resp.url)
    if resp.status_code == 200:
      return resp.json()
    return None
  
  def get_match(self, event_id: int):
    # https://betsapi.com/docs/events/view.html
    url = '/v1/event/view'
    params = { "event_id" : event_id}
    return self.request_api(url, params)

  def search_match(self, event_id:int):
    ...
  
  def get_ended_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # https://betsapi.com/docs/events/ended.html
    url = f'/v2/events/ended'
    params = {
      "league_id" : league_id,
      "sport_id": sport_id,
      "team_id": team_id
    }
    return self.request_api(url, params)
    
  def get_inplay_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # https://betsapi.com/docs/events/inplay.html
    url = f'/v2/events/inplay'
    params = {
      "league_id" : league_id,
      "sport_id": sport_id,
      "team_id": team_id
    }
    return self.request_api(url, params)

  def get_upcoming_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1, more_paramns = {}):
    # https://betsapi.com/docs/events/upcoming.html
    url = f'/v2/events/upcoming'
    params = {
      "league_id" : league_id,
      "sport_id": sport_id,
      "team_id": team_id
    }
    params.update(more_paramns)
    return self.request_api(url, params)

  def get_league(self, league_id:int, sport_id:int = 1):
    # https://betsapi.com/docs/events/league.html
    url = f'/v1/league'
    params = {
      "league_id" : league_id,
      "sport_id": sport_id
    }
    return self.request_api(url, params)

  def get_all_leagues(self, sport_id:int = 1, coutry:str = None, page:int =1):
    url = f'/v2/events/ended'
    params = {
      "sport_id" : sport_id,
      "coutry": coutry,
      "page": page
    }
    return self.request_api(url, params)

  def get_all_times(self, league_id:int, coutry:str = None, page:int =1):
    url = f'/v1/team'
    params = {
      "league_id" : league_id,
      "coutry": coutry,
      "page": page
    }
    return self.request_api(url, params)







# buscar ligas
# curl https://api.b365api.com/v1/league?token=YOUR_TOKEN&sport_id=1

# buscar liga
# https://api.b365api.com/v2/league/table?token=YOUR_TOKEN&league_id=94

# buscar times
# https://api.b365api.com/v1/team?token=YOUR_TOKEN&sport_id=1