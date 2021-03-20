from abc import ABC, abstractmethod

class IBetsAPI(ABC):

  BASE_URL = None
  TOKEN_API = None

  @abstractmethod
  def request_api(self, url:str, params:dict={}):
    ...

  @abstractmethod
  def get_game(self, event_id:int):
    ...

  @abstractmethod
  def get_ended_games(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of endeds football games
    ...

  @abstractmethod
  def get_inplay_games(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of inplay football games
    ...

  @abstractmethod
  def search_game(self, event_id:int):
    ...

  @abstractmethod
  def get_upcoming_games(self, league_id:int=None, team_id:int = None, sport_id = 1):
    # This method return a list of next football games
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