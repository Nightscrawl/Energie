from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExerciseType(models.Model):
    # exActions = [
    #     ('walk', 'Walking'),
    #     ('run', 'Running'),
    #     ('rband', 'Resistance Bands'),
    #     ('wtt', 'Weight Training'),
    #     ('warm', 'Warmup'),
    #     ('cool', 'Cooldown')
    # ]
    # exerciseTypeName=models.CharField(max_length=5, choices=exActions, default='walk')

    exerciseTypeName=models.CharField(max_length=255)

    def __str__(self):
        return self.exerciseTypeName
    
    class Meta:
        db_table='exercisetype'
        verbose_name_plural='exercisetypes'


class Exercise(models.Model):
    exerciseName=models.CharField(max_length=255)
    exerciseType=models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exerciseDate=models.DateField(default='mm/dd/yyyy')
    exerciseDurationMinutes=models.SmallIntegerField()
    exerciseNotes=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.exerciseName
    
    class Meta:
        db_table='exercise'
        verbose_name_plural='exercises'
