from django.core.management.base import BaseCommand
from quickies.models import QuickieLevel

class Command(BaseCommand):
    help = 'Seeds the QuickieLevel model with default levels and values.'

    def handle(self, *args, **kwargs):
        levels = [
            ("Beginner", 1),
            ("Intermediate", 2),
            ("Advanced", 3),
            ("Expert", 4),
            ("Elite", 5),
            ("Master", 6),
        ]

        for name, value in levels:
            obj, created = QuickieLevel.objects.get_or_create(ql_name=name, defaults={'ql_value': value})
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {name} ({value})"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {name} — skipping"))
