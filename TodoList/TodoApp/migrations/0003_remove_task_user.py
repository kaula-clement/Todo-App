# Generated by Django 4.0.5 on 2022-07-08 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
