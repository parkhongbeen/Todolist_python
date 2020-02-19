from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField('이름', max_length=100)


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    title = models.TextField(max_length=50)
    success = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

