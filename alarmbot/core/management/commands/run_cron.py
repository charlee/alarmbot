from croniter import croniter
from time import sleep
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from alarmbot.core.models import Task


class Command(BaseCommand):

    def handle(self, *args, **options):
        # wait until :00 second
        now = datetime.now()
        wait_secs = 60 - now.second - now.microsecond / 1000000
        print('Current time: %s, wait for %s seconds' % (now.isoformat(), wait_secs))
        sleep(wait_secs)

        while True:
            # query every minute
            now = datetime.now()
            print('Current time: %s, check tasks..' % now.isoformat())

            tasks = Task.objects.filter(enabled=True)
            for task in tasks:
                if croniter.match(task.cron, now):
                    # play task
                    print('  task %s (%s) matches, text=%s' % (task.id, task.cron, task.text))

            sleep(60)


