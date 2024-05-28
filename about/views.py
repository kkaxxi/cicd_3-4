from django.shortcuts import render
from django.http import HttpResponse


def about_view(request):
    return HttpResponse("<h1>About Page</h1>")


def index(request):
    return render(request, 'welcome.html')