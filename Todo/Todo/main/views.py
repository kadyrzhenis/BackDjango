from django.shortcuts import render
from datetime import datetime, timedelta

todos = [
        {
            'name': 'Finish the book',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=6),
            'owner': 'Zion',
            'mark': False
        },
        {
            'name': 'Buy the present',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=1),
            'owner': 'Zeke',
            'mark': False
        },
        {
            'name': 'Send the EA assignment',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=3),
            'owner': 'Zoe',
            'mark': True
        },
        {
            'name': 'Bake a banana bread',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=2),
            'owner': 'Zhenis',
            'mark': False
        },
        {
            'name': 'Try dance workouts',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=1),
            'owner': 'Zheka',
            'mark': True
        }

    ]


def todos_list(request):

    context = {
        'todos': todos
    }

    return render(request, 'todos_list.html', context=context)


def completed_todos_list(request):

    context = {
        'todos': todos
    }
    return render(request, 'completed_todos_list.html', context=context)

def index_page(request):
    return render(request, 'index.html')
