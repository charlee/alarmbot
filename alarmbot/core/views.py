import os
from django.views import View
from django.shortcuts import render, redirect
from alarmbot.core.models import Task
from alarmbot.core.tts import generate_tts_voice
from alarmbot.core.voice import get_voice_path
from alarmbot.core.player import play_mp3

def home(request):
    
    tasks = Task.objects.all()

    return render(request, 'index.html', { 'tasks': tasks })



class AddTaskView(View):

    def get(self, request):
        return render(request, 'tasks/add.html')

    def post(self, request):
        task_type_str = request.POST['task_type']
        text = request.POST['text']
        cron = request.POST['cron']

        if task_type_str == 'tts':
            task_type = Task.TaskType.tts

        task = Task.objects.create(task_type=task_type, text=text, cron=cron)

        # Generate synthetic voice
        if task_type_str == 'tts':
            generate_tts_voice(text, get_voice_path(task.id))

        return redirect('/')


class AdhocTaskView(View):

    def get(self, request):
        return render(request, 'tasks/adhoc.html')

    def post(self, request):
        text = request.POST['text']

        file = get_voice_path('adhoc')
        generate_tts_voice(text, file)
        play_mp3(file)

        return redirect('/tasks/adhoc')


class EnableTaskView(View):
    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.enabled = True
            task.save()

            return redirect('/')
        except Task.DoesNotExist:
            raise Http404


class DisableTaskView(View):
    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.enabled = False
            task.save()

            return redirect('/')
        except Task.DoesNotExist:
            raise Http404


class DeleteTaskView(View):
    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()

            voice_file = get_voice_path(id)
            if os.path.exists(voice_file):
                os.remove(voice_file)

            return redirect('/')
        except Task.DoesNotExist:
            raise Http404