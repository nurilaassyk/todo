from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextChoices
from simple_history.models import HistoricalRecords


class StatusChoices(TextChoices):
    TODO = 'todo', 'todo'
    IN_PROGRESS = 'in progress', 'in progress'
    DONE = 'done', 'done'


class Task(models.Model):
    task = models.CharField(null=False, blank=False, verbose_name='Task')
    description = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Description')
    status = models.TextField(verbose_name='Status',
                              choices=StatusChoices.choices,
                              max_length=100,
                              default=StatusChoices.TODO)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_task')
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executed_task')
    start_date = models.DateTimeField(verbose_name='Start date')
    end_date = models.DateTimeField(verbose_name='Expiration date')
    created_at = models.DateTimeField(verbose_name='Created date',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated date',
                                      auto_now_add=True)
    deleted_at = models.DateTimeField(verbose_name='Deleted date',
                                      auto_now_add=True)
    history = HistoricalRecords()
