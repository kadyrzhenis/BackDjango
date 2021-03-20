from django.http import Http404
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoListModelSerializer, TodoModelSerializer, TodoSerializer, TodoListSerializer
from .models import Todo, TodoList


# def login(request):
#     username = request.POST('username')
#     password = request.POST('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect("/todos")
#     else:
#         return HttpResponseRedirect("/")


class TodoListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = TodoList.objects.all()
        serializer = TodoListModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TodoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TodoListSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        todoList_data = request.data
        new_todoList = TodoList.objects.create(name=todoList_data['name'])
        new_todoList.save()
        serializer = TodoListModelSerializer(new_todoList)
        return Response(serializer.data)

    def destroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request):
        print(request.data['result'])


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()


class CompletedTodoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Todo.objects.filter(category='Completed')
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todos = Todo.objects.filter(category='Completed', list_id=pk)
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)

    def create(self, request):
        todo_data = request.data
        new_todo = Todo.objects.create(name=todo_data['name'], created_date=todo_data['created_date'],
                                       due_on_date=todo_data['due_on_date'], owner=todo_data['owner'],
                                       category=todo_data['category'], list_id=todo_data['list_id'])
        new_todo.save()
        serializer = TodoModelSerializer(new_todo)
        return Response(serializer.data)

    def destroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request):
        print(request.data['result'])
