from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('menu/', include('menu.urls')),
    path('', include('about.urls')),  # Включення about як головної сторінки
]
