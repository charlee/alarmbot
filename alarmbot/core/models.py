from django.db import models
from alarmbot.core.voice import get_voice_path

class Task(models.Model):

    class TaskType(models.IntegerChoices):
        tts = 1
        voice = 2

    cron = models.CharField(max_length=64)
    task_type = models.IntegerField(choices=TaskType.choices)
    text = models.CharField(max_length=400)
    enabled = models.BooleanField(default=True)

    def voice_url(self):
        return '/media/voices/voice-%s.mp3' % self.id

    def voice_file(self):
        return get_voice_path(self.id)