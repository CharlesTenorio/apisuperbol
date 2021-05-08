from django.contrib import admin
from django.utils.safestring import mark_safe

from sports.football.match.models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
  list_display = ['id','home', 'home_img', 'away_img','away', 'league_id', 'date', 'ss']
  list_filter = ['time_status', 'league_id'] 

  def date(self, obj:Match):
    return obj.event_date

  def home_img(self, obj:Match):
    if obj.home.image_big:
      return mark_safe(f"<img src='{obj.home.image_big}' width='30' height='30' />")
    return "Sem imagem"

  home_img.allow_tags = True
  home_img.__name__ = 'Escudo casa'

  
  def away_img(self, obj:Match):
    if obj.away.image_big:
      return mark_safe(f"<img src='{obj.away.image_big}' width='30' height='30' />")
    return "Sem imagem"

  away_img.allow_tags = True
  away_img.__name__ = 'Escudo Fora'