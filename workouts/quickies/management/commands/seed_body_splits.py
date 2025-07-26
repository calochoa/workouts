from django.core.management.base import BaseCommand
from quickies.models import BodySplit

class Command(BaseCommand):
    help = 'Seeds the BodySplit model with default split names.'

    def handle(self, *args, **kwargs):
        splits = [
            "Total Body",
            "Upper Body",
            "Lower Body",
            "Core"
        ]

        for name in splits:
            obj, created = BodySplit.objects.get_or_create(bs_name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {name} — skipping"))
