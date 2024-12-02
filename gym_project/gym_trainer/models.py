from django.db import models
from django.conf import settings

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        # ordering = ['-id']
        db_table = 'exercises'
    
class Routine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='routines')
    exercises = models.ManyToManyField(Exercise, related_name='routines')

    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # ordering = ['-created_at']
        db_table = 'routines'

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='schedules')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='schedules')
    hour = models.TimeField()

    class Meta:
        # ordering = ['-date', '-time']
        db_table = 'schedules'