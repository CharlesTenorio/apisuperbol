from django.contrib import admin
from bets.football.odds.models import Odd

class OddAdmin(admin.ModelAdmin):
  list_display = ['id', 'key']