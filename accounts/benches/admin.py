from django.contrib import admin
from accounts.benches.models import Bench

@admin.register(Bench)
class BenchAdmin(admin.ModelAdmin):
  list_display = ['name', 'user']
