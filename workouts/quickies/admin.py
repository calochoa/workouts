from django.contrib import admin
from .models import QuickieType, Level, BodySplit, Exercise, Quickie, QuickieExercise

admin.site.register(QuickieType)
admin.site.register(Level)
admin.site.register(BodySplit)
admin.site.register(Exercise)
admin.site.register(Quickie)
admin.site.register(QuickieExercise)