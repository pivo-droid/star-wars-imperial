from django.db import models


# Simple models for an "Imperial Database" project.
# - `Character` stores basic info about a character.
# - `Ship` stores a ship and links to its owning `Character`.


class Character(models.Model):
	name = models.CharField(max_length=200)
	species = models.CharField(max_length=100, blank=True)
	homeworld = models.CharField(max_length=100, blank=True)
	bio = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Ship(models.Model):
	name = models.CharField(max_length=200)
	model = models.CharField(max_length=200, blank=True)
	owner = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='ships')

	def __str__(self):
		return f"{self.name} ({self.model})" if self.model else self.name

