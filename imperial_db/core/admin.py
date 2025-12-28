from django.contrib import admin
from .models import Character, Ship


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'species', 'homeworld')
	search_fields = ('name', 'species', 'homeworld')


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'model', 'owner')
	search_fields = ('name', 'model', 'owner__name')

