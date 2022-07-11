from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User,related_name='tasks', on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=255,null=True)
    created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title