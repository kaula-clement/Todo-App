# Generated by Django 4.0.5 on 2022-07-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0004_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]