from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def addTask(request):
    # the 'task' is the name of our input field
    task = request.POST['task']
    # these are fields from the models.py, 
    # is_completed and date fields have default values, 
    # so they are not needed here
    Task.objects.create(task = task)
    return redirect('home')

def mark_as_done(request,pk):
    # fetches the specific record matching the  PK
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    # saves the update into the database
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    # fetches the specific record matching the  PK
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    # saves the update into the database
    task.save()
    return redirect('home')


def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)
    
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
    