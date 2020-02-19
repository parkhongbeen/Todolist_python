from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('todo_list/', views.todo_list, name='todo-list'),
    path('add_todo/', views.add_todo, name='add-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('edit_todo/<int:pk>', views.edit_todo, name='update-todo'),
    path('do_or_not/<int:pk>/', views.do_or_not_todo, name='do-todo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
