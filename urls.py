from django.contrib import admin
from django.urls import path, include
from about.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('menu/', include('menu.urls')),
    path('', index, name='index'),  # Включення about як головної сторінки
]
