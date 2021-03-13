from django.views import View
from django.shortcuts import render, redirect
from alarmbot.core.models import Task

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

        Task.objects.create(task_type=task_type, text=text, cron=cron)


        return redirect('/')
