from abc import ABC, abstractmethod
from bets.football.tickets.models import TicketOddMatch

class IConferenceOdd(ABC):

  def __init__(self, odd:TicketOddMatch):
    self.odd = odd
  

  @abstractmethod
  def conference(self):
    ...