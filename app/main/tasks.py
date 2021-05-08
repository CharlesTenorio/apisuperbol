from celery import shared_task


@shared_task
def import_today_matchs():
  """Essa função importa todos os jogos do dia"""
  ...


@shared_task
def update_odd_matchs():
  """Essa função atualiza os valores do odds"""
  ...
