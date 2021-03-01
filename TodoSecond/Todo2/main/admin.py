from django.contrib import admin

from main.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'due_on_date', 'owner', 'mark', ]
    ordering = ['id']
    search_fields = ['id', 'name', 'mark', 'due_on_date', ]
    list_filter = ['due_on_date', 'name', ]
