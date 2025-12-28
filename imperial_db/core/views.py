from django.shortcuts import render, get_object_or_404
from .models import Character, Ship


def character_list(request):
	"""Main page: show all characters."""
	characters = Character.objects.all().order_by('id')
	return render(request, 'core/character_list.html', {'characters': characters})


def character_detail(request, pk):
	"""Character page: show details and their ships."""
	character = get_object_or_404(Character, pk=pk)
	ships = character.ships.all()
	return render(request, 'core/character_detail.html', {'character': character, 'ships': ships})


def ship_detail(request, pk):
	"""Ship page: show ship details and link back to owner."""
	ship = get_object_or_404(Ship, pk=pk)
	return render(request, 'core/ship_detail.html', {'ship': ship})

