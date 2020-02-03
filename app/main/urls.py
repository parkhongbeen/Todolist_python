from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('edit_todo/<int:pk>', views.edit_todo, name='update-todo'),
]
