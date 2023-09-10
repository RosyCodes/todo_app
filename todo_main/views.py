from django.shortcuts import render
from todo.models import Task

def home(request):
    # fetches only incomplete tasks from mthe model and arranged by most recent
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks' : tasks,
    }
    return render(request,'home.html',context)