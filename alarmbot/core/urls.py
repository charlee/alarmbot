from django.urls import path, include
from alarmbot.core.views import home, AddTaskView

urlpatterns = [
    path('', home),
    path('tasks/add', AddTaskView.as_view()),
]