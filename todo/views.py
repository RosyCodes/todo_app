from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task

def addTask(request):
    # the 'task' is the name of our input field
    task = request.POST['task']
    # these are fields from the models.py, 
    # is_completed and date fields have default values, 
    # so they are not needed here
    Task.objects.create(task = task)
    return redirect('home')