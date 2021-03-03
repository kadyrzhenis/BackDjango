from django.shortcuts import render

from main.models import Todo


def todos_list(request):
    return render(request, 'todos_list.html', {'todos': Todo.objects.filter(mark=False)})


def completed_todos_list(request):
    return render(request, 'completed_todos_list.html', {'todos': Todo.objects.filter(mark=True)})


def index_page(request):
    return render(request, 'index.html')
