from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('todo_list', views.todo_list, name='todolist'),
    path('add_todo/', views.add_todo, name='add-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('edit_todo/<int:pk>', views.edit_todo, name='update-todo'),
    path('<int:pk>/do/', views.do_todo, name='do-todo'),
    path('<int:pk>/do_not/', views.do_not_todo, name='do-not-todo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
