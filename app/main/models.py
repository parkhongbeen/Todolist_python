from django.db import models


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
