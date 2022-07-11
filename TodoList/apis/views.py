from rest_framework.response import Response
from rest_framework.decorators import api_view
from TodoApp.models import Task
from .serializers import TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, generics, viewsets



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		'users':'/users/',
		}

	return Response(api_urls)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['POST'])
def taskCreate(request):
	user=request.user
	owner=Task(owner=user)
	serializer = TaskSerializer(owner,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

	

@api_view(['GET'])
def taskList(request):
	tasks=Task.objects.filter(owner=request.user)
	serializer=TaskSerializer(tasks,many=True)
	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	if task.owner != user:
		return Response('You are not owner')
	elif serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	
	task = Task.objects.get(id=pk)
	user=request.user
	if task.owner != user:
		return Response('You are not owner')
	task.delete()
	return Response('Item succsesfully delete!')



#==================================================================================

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
	
#===================================================================================

