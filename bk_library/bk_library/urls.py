from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ebook.urls')),
    path('', include('registration.urls'))
]










