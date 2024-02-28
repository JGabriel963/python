from django.contrib import admin
from soccer.models import Clube, Jogador

class JogadorInline(admin.StackedInline):
    model = Jogador
    extra = 0

# Register your models here.
@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_fundacao', 'divisao']
    list_filter = ['divisao', 'modalidade']
    search_fields = ['nome']

    inlines = [JogadorInline]