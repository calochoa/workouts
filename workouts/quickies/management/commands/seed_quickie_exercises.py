import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from quickies.models import Quickie, Exercise, QuickieExercise

class Command(BaseCommand):
    help = 'Seeds the QuickieExercise model from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv',
            type=str,
            help='Path to the CSV file (relative to BASE_DIR)',
            required=True,
        )

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, options['csv'])

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f"CSV file not found: {csv_path}"))
            return

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                q_name = row['quickie_name'].strip()
                e_name = row['exercise_name'].strip()
                reps = int(row['reps'])
                order = int(row['order'])

                try:
                    quickie = Quickie.objects.get(q_name=q_name)
                    exercise = Exercise.objects.get(e_name__iexact=e_name)
                except Quickie.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Quickie not found: {q_name}"))
                    continue
                except Exercise.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Exercise not found: {e_name}"))
                    continue

                exists = QuickieExercise.objects.filter(
                    quickie=quickie,
                    exercise=exercise,
                    order=order
                ).exists()

                if exists:
                    self.stdout.write(self.style.WARNING(f"Already exists: {q_name} - {e_name} (#{order}) — skipping"))
                    continue

                QuickieExercise.objects.create(
                    quickie=quickie,
                    exercise=exercise,
                    reps=reps,
                    order=order
                )
                self.stdout.write(self.style.SUCCESS(f"Created: {q_name} - {e_name} ({reps} reps, order {order})"))
