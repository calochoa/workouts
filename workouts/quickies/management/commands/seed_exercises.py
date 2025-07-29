import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from quickies.models import Exercise, Level, BodySplit

class Command(BaseCommand):
    help = 'Seeds or updates the Exercise model from a JSON file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json',
            type=str,
            help='Path to the JSON file (relative to BASE_DIR)',
            required=True,
        )

    def handle(self, *args, **options):
        json_path = os.path.join(settings.BASE_DIR, options['json'])

        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f"JSON file not found: {json_path}"))
            return

        with open(json_path, 'r', encoding='utf-8') as f:
            exercises = json.load(f)

        created, updated, skipped = 0, 0, 0

        for entry in exercises:
            e_name = entry.get('e_name')
            level_value = entry.get('e_level')
            body_split_id = entry.get('e_body_split')
            e_youtube_id = entry.get('e_youtube_id')
            e_description = entry.get('e_description', {})  # keep as JSON

            try:
                level = Level.objects.get(l_value=level_value)
            except Level.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Missing Level (l_value={level_value}) for {e_name}"))
                skipped += 1
                continue

            body_split = None
            if body_split_id:
                try:
                    body_split = BodySplit.objects.get(id=body_split_id)
                except BodySplit.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Missing BodySplit (id={body_split_id}) for {e_name}"))
                    skipped += 1
                    continue

            obj, created_flag = Exercise.objects.update_or_create(
                e_name=e_name,
                defaults={
                    'e_level': level,
                    'e_body_split': body_split,
                    'e_youtube_id': e_youtube_id,
                    'e_description': e_description  # store as structured JSON
                }
            )

            if created_flag:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {e_name}"))
            else:
                updated += 1
                self.stdout.write(self.style.WARNING(f"Updated: {e_name}"))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. Created: {created}, Updated: {updated}, Skipped: {skipped}"
        ))
