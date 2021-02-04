from django.contrib import admin
from .models import Cambista

class CambistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_banca', 'nome','cpf')
    search_fields = ('nome', )

admin.site.register(Cambista, CambistaAdmin)


