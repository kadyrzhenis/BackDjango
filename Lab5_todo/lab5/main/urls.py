from django.urls import path
from main.views import TodoListViewSet, TodoViewSet, CompletedTodoViewSet

urlpatterns = [
    path('todos', TodoViewSet.as_view({'get': 'list'})),
    path('todos/<int:pk>', TodoListViewSet.as_view({'get': 'retrieve'})),
    path('todos/<int:pk>/completed', CompletedTodoViewSet.as_view({'get': 'retrieve'})),
]