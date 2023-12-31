# Generated by Django 4.2.4 on 2023-08-18 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(verbose_name='Task')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('status', models.TextField(choices=[('todo', 'todo'), ('in progress', 'in progress'), ('done', 'done')], default='todo', max_length=100, verbose_name='Status')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='Expiration date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated date')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='Deleted date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_task', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executed_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(verbose_name='Project')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='Expiration date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='Deleted date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executed_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('task', models.CharField(verbose_name='Task')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('status', models.TextField(choices=[('todo', 'todo'), ('in progress', 'in progress'), ('done', 'done')], default='todo', max_length=100, verbose_name='Status')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='Expiration date')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated date')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Deleted date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('project', models.CharField(verbose_name='Project')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='Expiration date')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created date')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Deleted date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical project',
                'verbose_name_plural': 'historical projects',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
