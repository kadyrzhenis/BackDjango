from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    due_on_date = models.DateTimeField()
    owner = models.CharField(max_length=100)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.name
