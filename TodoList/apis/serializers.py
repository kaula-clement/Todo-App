from rest_framework import serializers
from TodoApp.models import Task
from django.contrib.auth.models import User


class TaskSerializer( serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['title','description','created','completed']
        
        

class UserSerializer(serializers.ModelSerializer):
    tasks=serializers.PrimaryKeyRelatedField(many=True,queryset=Task.objects.all())
    class Meta:
        model = User
        #fields = ['id', 'username','tasks']
        fields='__all__'