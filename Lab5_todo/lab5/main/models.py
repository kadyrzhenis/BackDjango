from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    due_on_date = models.DateTimeField()
    owner = models.CharField(max_length=100)
    list_id = models.ForeignKey(TodoList, on_delete=models.RESTRICT, related_name='todos')
    category = models.CharField(max_length=40, default='Incomplete')

    class Meta:
        ordering = ['id']
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'

    def __str__(self):
        return self.name
