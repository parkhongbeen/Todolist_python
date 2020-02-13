from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Todo
from .forms import PostCreateForm, TodoUpdateForm, LoginForm, SignupForm


def todo_list(request):
    todo = Todo.objects.all().order_by('-pk')
    context = {
        'todo_list': todo
    }
    return render(request, 'main/todo-list.html', context)


def search_todo(request):
    queryset = Todo.objects.all()
    search = request.GET.get('search', '')

    if search:
        queryset = queryset.filter(title__icontains=search)

        # get 은 데이터 하나를 가지고옴. ex: hello 를 검색창에 치면, 찾은 첫번째 데이터를 가지고옴
        # filter 는 hello 가 들어간 모든 데이터를 가지고온다

    return render(request, 'main/todo-list.html', {
        'search_todo': queryset,
    })


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
        return redirect('main:todo-list')
    else:
        form = PostCreateForm()
        context = {
            'form': form,
        }
    return render(request, 'main/todo-list.html', context)


def delete_todo(reqeust, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:todo-list')


def edit_todo(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo.objects.get(pk=pk)
        todo.title = title
        todo.text = text
        todo.save()
        return redirect('main:todo-list')
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
    return redirect('main:todo-list')


def do_not_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.success = False
    todo.save()
    return redirect('main:todo-list')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('main:todo-list')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)


def signup_view(request):
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
