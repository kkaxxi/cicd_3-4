# menu/views.py
from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})
