from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Todo
from .forms import PostCreateForm, TodoUpdateForm, LoginForm, SignupForm


def todo_list(request):
    todo_list = Todo.objects.all().order_by('-pk')
    context = {
        'todo_list': todo_list
    }
    return render(request, 'main/todolist.html', context)


def add_todo(request):
    if request.method == 'POST':
        text = request.POST['text']
        title = request.POST['title']
        todo = Todo.objects.create(
            title=title,
            text=text,
            user=request.user,
        )
        todo.save()
        return redirect('main:todolist')
    else:
        form = PostCreateForm()
        context = {
            'form': form,
        }
    return render(request, 'main/todolist.html', context)


def delete_todo(reqeust, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:todolist')


def edit_todo(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo.objects.get(pk=pk)
        todo.title = title
        todo.text = text
        todo.save()
        return redirect('main:todolist')
    else:
        form = TodoUpdateForm()
        todo = Todo.objects.get(pk=pk)
        context = {
            'todo': todo,
            'form': form,
        }
        return render(request, 'main/todo_edit.html', context)


def do_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    # user = request.user

    todo.success = True
    todo.save()
    return redirect('main:todolist')


def do_not_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.success = False
    todo.save()
    return redirect('main:todolist')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('main:todolist')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)


def Signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'main/login.html')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'main/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('main:login')
