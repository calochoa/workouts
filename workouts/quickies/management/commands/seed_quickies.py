from django.core.management.base import BaseCommand
from quickies.models import Quickie, QuickieType, Level, BodySplit
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the Quickie model with predefined data'

    def handle(self, *args, **kwargs):
        entries = [
            # Format: (name, type, level, body_split)
            ("Quick Core", "Junior", "Beginner", "Core"),
            ("Quick Pack", "Junior", "Beginner", "Core"),
            ("Quick Easy", "Junior", "Beginner", "Total Body"),
            ("Quick Start", "Junior", "Beginner", "Total Body"),
            ("Quick Burn", "Junior", "Beginner", "Lower Body"),
            ("Quick Pump", "Junior", "Beginner", "Total Body"),
            ("Quick Silver", "Junior", "Beginner", "Upper Body"),
            ("Quick Evo", "Junior", "Beginner", "Lower Body"),
            ("Quick Up", "Junior", "Beginner", "Upper Body"),
            ("Quick One", "Junior", "Beginner", "Total Body"),
            ("Quick Burst", "Junior", "Beginner", "Total Body"),
            ("Quick n Dirty", "Junior", "Beginner", "Total Body"),
            ("Bread & Butter", "Basic", "Intermediate", "Total Body"),
            ("Core Galore", "Basic", "Intermediate", "Core"),
            ("Heating Up", "Basic", "Intermediate", "Lower Body"),
            ("Boot Camp", "Basic", "Advanced", "Total Body"),
            ("Hard Core", "Basic", "Advanced", "Core"),
            ("Push-Up or Shut Up", "Basic", "Expert", "Upper Body"),
            ("Too Easy", "Basic", "Expert", "Upper Body"),
            ("BurpeEvo", "Basic", "Advanced", "Total Body"),
            ("Core Time", "Basic", "Intermediate", "Core"),
            ("Ab Time", "Basic", "Advanced", "Core"),
            ("Six Pack", "Basic", "Expert", "Core"),
            ("Harder Core", "Basic", "Expert", "Core"),
            ("Up and Down", "Basic", "Advanced", "Lower Body"),
            ("Shape Up", "Basic", "Intermediate", "Upper Body"),
            ("Step It Up", "Basic", "Advanced", "Upper Body"),
            ("Do It Now", "Basic", "Advanced", "Upper Body"),
            ("Nothing Special", "Basic", "Intermediate", "Upper Body"),
            ("Hip-Hop U Dont Stop", "Cardio", "Intermediate", "Lower Body"),
            ("Bang Bang Boogie", "Cardio", "Intermediate", "Total Body"),
            ("Beach Body", "Cardio", "Expert", "Total Body"),
            ("Go Hard", "Cardio", "Advanced", "Total Body"),
            ("Hot In Here", "Cardio", "Advanced", "Lower Body"),
            ("Cant Stop Wont Stop", "Cardio", "Expert", "Lower Body"),
            ("En Fuego", "Cardio", "Expert", "Total Body"),
            ("Evolution", "Cardio", "Expert", "Total Body"),
            ("Leg-endary", "Cardio", "Expert", "Lower Body"),
            ("Mondays", "Cardio", "Intermediate", "Total Body"),
            ("24/7", "Cardio", "Intermediate", "Total Body"),
            ("Nap Time", "Cardio", "Intermediate", "Total Body"),
            ("I Got This", "Cardio", "Intermediate", "Total Body"),
            ("Muffin Tops", "Cardio", "Advanced", "Total Body"),
            ("Wake Up", "Cardio", "Advanced", "Total Body"),
            ("Jump Start", "Cardio", "Advanced", "Lower Body"),
            ("Some Day", "Cardio", "Expert", "Total Body"),
            ("Quick Bar Starzz", "Bar", "Beginner", "Total Body"),
            ("Quick Barz", "Bar", "Beginner", "Upper Body"),
            ("Baby Cobra", "Bar", "Intermediate", "Upper Body"),
            ("Hang Time", "Bar", "Advanced", "Core"),
            ("Bar Core", "Bar", "Advanced", "Core"),
            ("Pull-Up or Shut Up", "Bar", "Expert", "Upper Body"),
            ("King Cobra", "Bar", "Expert", "Upper Body"),
            ("Bar Evolution", "Bar", "Expert", "Total Body"),
            ("Hanging Around", "Bar", "Intermediate", "Total Body"),
            ("Bar Fun", "Bar", "Expert", "Total Body"),
            ("Power Pack", "Power", "Elite", "Core"),
            ("Turtle Power", "Power", "Elite", "Total Body"),
            ("Balance of Power", "Power", "Elite", "Total Body"),
            ("Power Up", "Power", "Elite", "Upper Body"),
            ("Power Struggle", "Power", "Elite", "Total Body"),
            ("Rise to Power", "Power", "Elite", "Total Body"),
            ("Max Power", "Power", "Elite", "Total Body"),
            ("Power Evolution", "Power", "Elite", "Total Body"),
            ("Core Power", "Power", "Elite", "Core"),
            ("Power Burst", "Power", "Elite", "Lower Body"),
            ("Powerful", "Power", "Elite", "Lower Body"),
            ("Power Hitter", "Power", "Elite", "Upper Body"),
            ("Absolute Power", "Power", "Elite", "Total Body"),
            ("Power Play", "Power", "Elite", "Total Body"),
            ("NOT Easy", "Ultimate", "Master", "Total Body"),
            ("Bar Starzz", "Ultimate", "Master", "Total Body"),
            ("Jungle Gym", "Ultimate", "Master", "Core"),
            ("Ultimate Evolution", "Ultimate", "Master", "Total Body"),
            ("Upper Stretchie #1", "Stretchies", "Beginner", "Upper Body"),
            ("Upper Stretchie #2", "Stretchies", "Beginner", "Upper Body"),
            ("Upper Stretchie #3", "Stretchies", "Beginner", "Upper Body"),
            ("Upper Stretchie #4", "Stretchies", "Beginner", "Upper Body"),
            ("Lower Stretchie #1", "Stretchies", "Intermediate", "Lower Body"),
            ("Lower Stretchie #2", "Stretchies", "Intermediate", "Lower Body"),
        ]

        for name, type_name, level_name, body_split_name in entries:
            try:
                qtype = QuickieType.objects.get(qt_name=type_name)
                level = Level.objects.get(l_name=level_name)
                body_split = BodySplit.objects.get(bs_name=body_split_name)
            except (QuickieType.DoesNotExist, Level.DoesNotExist, BodySplit.DoesNotExist) as e:
                self.stdout.write(self.style.ERROR(f"Missing related object for '{name}': {e}"))
                continue

            obj, created = Quickie.objects.get_or_create(
                q_name=name,
                defaults={
                    'q_type': qtype,
                    'q_level': level,
                    'q_body_split': body_split,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {name} — skipping"))
