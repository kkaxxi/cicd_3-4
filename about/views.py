# about/views.py
from django.shortcuts import render
from .models import About

def about_view(request):
    about_info = About.objects.all()
    return render(request, 'about/about.html', {'about_info': about_info})

def index(request):
    return render(request, 'welcome.html')
