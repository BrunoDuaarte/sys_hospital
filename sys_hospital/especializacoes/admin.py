from django.contrib import admin
from .models import Especializacoes

@admin.register(Especializacoes)
class EspecializacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

