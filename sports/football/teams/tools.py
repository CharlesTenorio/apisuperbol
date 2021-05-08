from sports.football.teams.models import Team


def get_or_create_team(team:dict):
  team, _ = Team.objects.get_or_create(
    id = team['id'],
    name = team['name'],
    cc = team['cc'],
    image_id = team['image_id']
  )
  return team