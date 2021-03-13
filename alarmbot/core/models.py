from django.db import models

class Task(models.Model):

    class TaskType(models.IntegerChoices):
        tts = 1
        voice = 2

    cron = models.CharField(max_length=64)
    task_type = models.IntegerField(choices=TaskType.choices)
    text = models.CharField(max_length=400)