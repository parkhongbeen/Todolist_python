from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo


def index(request):
    todo_list = Todo.objects.all().order_by('-pk')
    context = {
        'todo_list': todo_list
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    currunt_date = timezone.now()
    text = request.POST['text']
    Todo.objects.create(created=currunt_date, text=text)
    return redirect('main:index')


def delete_todo(reqeust, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:index')


def edit_todo(request, pk):
    if request.method == 'POST':
        text = request.POST['text']
        todo = Todo.objects.get(pk=pk)
        todo.text = text
        todo.save()
        return redirect('main:index')
    else:
        todo = Todo.objects.get(pk=pk)
        context = {
            'todo': todo,
        }
        return render(request, 'main/todo_edit.html', context)

