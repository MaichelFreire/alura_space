from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'name', 'subtitle', 'foto')
    list_display_links = ('id', 'name', 'foto')




admin.site.register(Fotografia, ListandoFotografias)