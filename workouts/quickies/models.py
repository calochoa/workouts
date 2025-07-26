import datetime
from django.db import models

class QuickieType(models.Model):
    qt_name = models.CharField(max_length=64)

    def __str__(self):
        return (f"ID: {self.id}, Type: {self.qt_name}")

class Level(models.Model):
    l_name = models.CharField(max_length=64)
    l_value = models.IntegerField()

    def __str__(self):
        return (f"ID: {self.id}, Name (Value): {self.l_name} ({self.l_value})")

class BodySplit(models.Model):
    bs_name = models.CharField(max_length=64)

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.bs_name}")

class Exercise(models.Model):
    e_name = models.CharField(max_length=64)
    e_level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.e_name}, Level: {self.e_level.l_name}")

class Quickie(models.Model):
    q_name = models.CharField(max_length=64)
    q_type = models.ForeignKey(QuickieType, on_delete=models.CASCADE)
    q_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    q_body_split = models.ForeignKey(BodySplit, on_delete=models.CASCADE)
    youtube_id = models.CharField(max_length=64, blank=True, null=True)
    date_created = models.DateField(default=datetime.date(2019, 8, 13))

    def youtube_url(self):
        return(f"https://www.youtube.com/watch?v={self.youtube_id}")
    
    def youtube_thumbnail(self):
        return(f"https://img.youtube.com/vi/{self.youtube_id}/hqdefault.jpg")

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"Name: {self.q_name}, "
            f"Type: {self.q_type.qt_name}, "
            f"Level: {self.q_level.l_name}, "
            f"Body Split: {self.q_body_split.bs_name}, "
            f"YouTube ID: {self.youtube_id}, "
            f"Date Created: {self.date_created}"
        )

class QuickieExercise(models.Model):
    quickie = models.ForeignKey(Quickie, on_delete=models.CASCADE, related_name='quickie_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    order = models.PositiveSmallIntegerField()  # 1, 2, 3, etc.

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.reps} reps of {self.exercise.e_name} (#{self.order})"
