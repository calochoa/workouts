from django.core.management.base import BaseCommand
from quickies.models import QuickieType

class Command(BaseCommand):
    help = 'Seeds the QuickieType model with default types.'

    def handle(self, *args, **kwargs):
        types = [
            "Junior", 
            "Basic", 
            "Cardio", 
            "Bar", 
            "Power", 
            "Ultimate", 
            "Stretchies"
        ]

        for t in types:
            obj, created = QuickieType.objects.get_or_create(qt_name=t)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {t}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {t} — skipping"))
