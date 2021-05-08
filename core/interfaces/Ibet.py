from abc import ABC, abstractmethod, abstractproperty

class IBetsAPI(ABC):
  
  BASE_URL = None
  TOKEN_API = None

  @abstractmethod
  def request_api(self, url:str, params:dict={}):
    ...

  @abstractmethod
  def get_match(self, event_id:int):
    ...

  @abstractmethod
  def get_ended_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of endeds football matchs
    ...

  @abstractmethod
  def get_inplay_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of inplay football matchs
    ...

  @abstractmethod
  def search_match(self, event_id:int):
    ...

  @abstractmethod
  def get_upcoming_matchs(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of next football matchs
    ...

  @abstractmethod
  def get_league(self, league_id:int, sport_id:int = 1):
    ...

  @abstractmethod
  def get_all_leagues(self, sport_id:int = 1, coutry:str = None, page:int =1):
    ...

  @abstractmethod
  def get_all_times(self, league_id:int, coutry:str = None, page:int =1):
    ...