from services.bets.bets365.api import Bets365API
from sports.football.match.tools import get_or_create_match

class Bets365Handler:

  api = Bets365API()

  def claen_blank_paramns(self, params:dict) -> dict:
    return {key:value for key,value in params.items() if value}

  def get_upcoming_matchs(self, cc:str=None, day:str=None, page:int=None) -> dict:
    more_params = self.claen_blank_paramns({ "cc": cc, "day": day, "page": page })
    if events := self.api.get_upcoming_matchs(more_paramns=more_params):
      return events

  def import_matchs(self):
    today = self.api.get_today_to_api()
    current_page = 1
    if events := self.get_upcoming_matchs(day=today, page=current_page):
      total = events.get('pager').get('total')
      per_page = events.get('pager').get('per_page')
      print(int(total / per_page))
      while len(events.get('results')) > 0:
        for event in events.get('results', []):
          get_or_create_match(event=event)

        current_page +=1
        events = self.get_upcoming_matchs(day=today, page=current_page)
        print(current_page)
        

