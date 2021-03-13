from croniter import croniter
from time import sleep
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from alarmbot.core.models import Task
from alarmbot.core.player import play_mp3


class Command(BaseCommand):

    def handle(self, *args, **options):
        # wait until :00 second
        now = timezone.localtime()
        wait_secs = 60 - now.second - now.microsecond / 1000000
        print('Current time: %s, wait for %s seconds' % (now.isoformat(), wait_secs))
        sleep(wait_secs)

        while True:
            # query every minute
            now = timezone.localtime()
            print('Current time: %s, check tasks..' % now.isoformat())

            tasks = Task.objects.filter(enabled=True)
            for task in tasks:
                if croniter.match(task.cron, now):
                    # play task
                    print('  task %s (%s) matches, text=%s' % (task.id, task.cron, task.text))
                    play_mp3(task.voice_file())

            sleep(60)


