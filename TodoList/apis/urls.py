from django.urls import path
from rest_framework import routers
from . import views

#from .views import TaskViewSet



urlpatterns=[
	path('users/',views.UserList.as_view()),
    path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.TaskDetail.as_view(), name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

]
