from django.core.management.base import BaseCommand

from core.models import Character, Ship


class Command(BaseCommand):
    help = 'Populate the DB with 82 placeholder Imperial characters and one ship each.'

    def handle(self, *args, **options):
        created_chars = 0
        for i in range(1, 83):
            name = f'Imperial Character {i}'
            char, created = Character.objects.get_or_create(name=name, defaults={
                'species': 'Human' if i % 3 else 'Droid',
                'homeworld': 'Coruscant' if i % 2 else 'Unknown',
                'bio': f'Automatically generated placeholder bio for {name}.',
            })
            if created:
                created_chars += 1

            ship_name = f'Ship of {char.name}'
            Ship.objects.get_or_create(name=ship_name, owner=char, defaults={'model': f'Model-{i}'})

        self.stdout.write(self.style.SUCCESS(f'Population complete. Characters created: {created_chars}'))
