from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    context = {
        'name': 'Zhenis',
        'id': '1',
        'status': 'student',
    }
    return render(request, 'index.html', context=context)


def current_datetime(request):
    return HttpResponse(datetime.now())


def time_plus(request):
    if request.GET['hours']:
        dt = datetime.now() + timedelta(hours=int(request.GET['hours']))
        return HttpResponse(dt)
    return HttpResponse('null')


def hours_ahead(request, hours, days):
    dt = datetime.now() + timedelta(days=days, hours=hours)
    return HttpResponse(dt)
