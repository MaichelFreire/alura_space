from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'name', 'subtitle', 'foto')
    list_display_links = ('id', 'name', 'foto')
    search_fields = ('id', 'name')
    list_filter = ('categoria', )





admin.site.register(Fotografia, ListandoFotografias)