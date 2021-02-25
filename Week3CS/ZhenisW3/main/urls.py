from django.urls import path, re_path

from main.views import index, current_datetime, time_plus, hours_ahead

urlpatterns = [
    path('', index),
    path('time/plus/', time_plus),
    path('time/plus/<int:hours>/<int:days>/', hours_ahead)
]