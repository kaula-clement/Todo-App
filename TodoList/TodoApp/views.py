from django.shortcuts import render
import requests
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView 
from django.views.generic.edit import FormView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name='TodoApp/Login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name='TodoApp/Register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage, self).form_valid(form)

"""
def home(LoginRequiredMixin,request):
    return render (request, 'Task.html')

"""
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'


