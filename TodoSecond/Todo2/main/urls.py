from django.urls import path

from main.views import todos_list, completed_todos_list, index_page

urlpatterns = [
    path('todos', todos_list),
    path('todos/1/completed', completed_todos_list),
    path('', index_page),
]