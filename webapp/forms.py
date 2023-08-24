from django import forms

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'description', 'status', 'author', 'executor', 'start_date', 'end_date')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")
