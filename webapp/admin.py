from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from webapp.models import Task


class TaskHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['task', 'description', 'status', 'author', 'executor', 'start_date', 'end_date']
    fields = ['task', 'description', 'status', 'author', 'executor', 'start_date', 'end_date']
    history_list_display = ["status"]


admin.site.register(Task, TaskHistoryAdmin)
