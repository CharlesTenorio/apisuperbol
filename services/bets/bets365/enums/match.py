from django.db.models import TextChoices

class TimeStatusChoices(TextChoices):
  NOT_STARTED = '0', 'Not Started'
  IN_PLAY = '1', 'InPlay'
  TO_BE_FIXED = '2', 'TO BE FIXED'
  ENDED = '3', 'Ended'
  POSTPONED = '4', 'Postponed'
  CANCELLED = '5', 'Cancelled'
  WALKOVER = '6', 'Walkover'
  INTERRUPTED = '7', 'Interrupted'
  ABANDONED = '8', 'Abandoned'
  RETIRED = '9', 'Retired'
  REMOVED = '99', 'Removed'