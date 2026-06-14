from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
# Create your views here.

 

def task_list(request):
    if request.method == "POST":
        task = request.POST.get('task')

         
        Task.objects.create(task = task)

        return redirect("todo:task_list")
     
    tasks = Task.objects.all()
    
    return render(request, 'todo/task_list.html',{
        'tasks':tasks
    })



def edit_Task(request, task_id):
    task_obj = get_object_or_404(Task, pk = task_id)

    if request.method == "POST":
        task_obj.task = request.POST.get('task')
        task_obj.save()

        return redirect("todo:task_list")
    
    return render(request, 'todo/editTask.html',{
        'task': task_obj,
         
    })

def delete_Task(request, delete_id):
    delete_task = get_object_or_404(Task, pk = delete_id)

    if request.method == "POST":
        delete_task.delete()

        return redirect('todo:task_list')

    return render(request, 'todo/deleteTask.html',{
        'deleteTask': delete_task
    })





