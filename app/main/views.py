from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    currunt_date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=currunt_date, text=content)
    return redirect('main:index')


def delete_todo(reqeust, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:index')
