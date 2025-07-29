from django.core.management.base import BaseCommand
from quickies.models import Exercise, Level

class Command(BaseCommand):
    help = 'Seeds the Exercise model with default exercise names and associated levels.'

    def handle(self, *args, **kwargs):
        exercise_data = [
            (5, "atomic tricep blasters"),
            (4, "behind the neck pull-ups"),
            (2, "bicycle crunches"),
            (2, "box squats"),
            (6, "burpee muscle-ups"),
            (5, "burpee pull-ups"),
            (5, "burpee tuck jumps"),
            (4, "burpees"),
            (1, "calf jumps"),
            (1, "calf raises"),
            (3, "chest-ups"),
            (4, "chin-ups"),
            (6, "clapping pull-ups"),
            (5, "clapping push-ups"),
            (4, "commando pull-ups"),
            (1, "criss cross scissors"),
            (1, "crunch kicks"),
            (1, "crunches"),
            (3, "decline push-ups"),
            (4, "dips"),
            (1, "forward backward hops"),
            (1, "four square hops"),
            (6, "front lever swings"),
            (3, "full-body crunches"),
            (3, "half-wipers"),
            (6, "handstand push-ups"),
            (4, "hanging criss cross scissors"),
            (3, "hanging hurdles"),
            (3, "hanging knee raises"),
            (4, "hanging leg raises"),
            (4, "hanging leg rotations"),
            (3, "hanging oblique raises"),
            (4, "hanging open close scissors"),
            (6, "hanging shoot-ups"),
            (4, "hanging up down scissors"),
            (6, "hanging wipers"),
            (2, "heiden hops"),
            (1, "high knees"),
            (1, "incline push-ups"),
            (3, "inverted rows"),
            (3, "jumping chin-ups"),
            (1, "jumping jacks"),
            (4, "jumping lunges"),
            (3, "jumping pull-ups"),
            (1, "knee strikes"),
            (5, "L sit pull-ups"),
            (2, "leg raises"),
            (2, "lunges"),
            (2, "mountain climbers"),
            (6, "muscle-ups"),
            (1, "open close scissors"),
            (5, "pistol squats"),
            (2, "plank jacks"),
            (4, "pull-ups"),
            (3, "push-ups"),
            (1, "rolling sit-ups"),
            (3, "seated dips"),
            (2, "shoot-ups"),
            (1, "side crunches"),
            (1, "side-to-side hops"),
            (5, "side-to-side pull-ups"),
            (6, "single-arm push-ups"),
            (3, "sit-ups"),
            (4, "spiderman push-ups"),
            (3, "squat jumps"),
            (4, "tuck jumps"),
            (1, "up down scissors"),
            (4, "wipers"),
            (1, "small arm circles"),
            (1, "reverse small arm circles"),
            (1, "large arm circles"),
            (1, "reverse large arm circles"),
            (1, "lateral arm raises"),
            (1, "front arm raises"),
            (1, "lateral rotator cuffs"),
            (1, "front rotator cuffs"),
            (1, "low arm criss crosses"),
            (1, "arm criss crosses"),
            (1, "high arm criss crosses"),
            (1, "running arm swings"),
            (1, "neck up-downs"),
            (1, "neck side-to-sides"),
            (1, "neck leans"),
            (1, "neck rotations"),
            (2, "heel-to-glutes"),
            (2, "knee hugs"),
            (2, "ankle hugs"),
            (2, "toe touches"),
            (2, "lateral leg swings"),
            (2, "front leg swings"),
            (2, "high hurdles"),
            (2, "reverse high hurdles"),
        ]

        created = 0
        skipped = 0

        for level_value, exercise_name in exercise_data:
            try:
                level = Level.objects.get(l_value=level_value)
                obj, created_flag = Exercise.objects.get_or_create(
                    e_name=exercise_name,
                    defaults={'e_level': level}
                )
                if created_flag:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {exercise_name} (Level {level_value})"))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(f"Already exists: {exercise_name} — skipping"))
            except Level.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Level with l_value={level_value} does not exist — skipping {exercise_name}"))

        self.stdout.write(self.style.SUCCESS(f"\nDone. Created: {created}, Skipped: {skipped}"))
