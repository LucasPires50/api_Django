from django.contrib import admin
from estoque.models import EstoqueInterno

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_link = ('nome', 'valor')
    search_fields = ('nome', )

admin.site.register(EstoqueInterno, Produtos)