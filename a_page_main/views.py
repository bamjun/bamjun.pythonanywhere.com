import datetime

from django.shortcuts import render


def home(request):
    time = datetime.datetime.now()
    return render(request, "home.html", {"time": time})
