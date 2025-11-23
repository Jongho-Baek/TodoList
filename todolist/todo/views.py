from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(user=request.user, title=title)
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')

