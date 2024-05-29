from django.shortcuts import render
from django.http import HttpResponse  # Додати цей імпорт
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Message sent successfully")
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
