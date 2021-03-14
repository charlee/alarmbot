from django.urls import path, include
import alarmbot.core.views as home_views

urlpatterns = [
    path('', home_views.home),
    path('tasks/add', home_views.AddTaskView.as_view()),
    path('tasks/adhoc', home_views.AdhocTaskView.as_view()),
    path('tasks/enable/<int:id>/', home_views.EnableTaskView.as_view()),
    path('tasks/disable/<int:id>/', home_views.DisableTaskView.as_view()),
    path('tasks/delete/<int:id>/', home_views.DeleteTaskView.as_view()),
]