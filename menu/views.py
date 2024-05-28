from django.shortcuts import render
from django.http import HttpResponse


def menu_view(request):
    return HttpResponse("<h1>Menu Page</h1>")
