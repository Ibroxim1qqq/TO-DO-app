from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    if request.method == "POST":
        title = request.POST["title"]
        new_task = Task(title=title)
        new_task.save()

    tasks = Task.objects.all()
    return render(request, 'index.html', {"tasks": tasks})


def toggle_done(request, pk): 
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def delete_task(request, pk): 
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')
    return render(request, 'update.html', {'task': task})
  
