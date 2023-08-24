from django.urls import path

from webapp.views import IndexView, TaskCreateView, TaskDetailView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/add', TaskCreateView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit', TaskEditView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]
