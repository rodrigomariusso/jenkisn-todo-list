# Generated by Django 2.1.7 on 2019-03-07 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_completed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 3, 7, 15, 0, 36, 987938)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(blank=True, max_length=280),
        ),
    ]
