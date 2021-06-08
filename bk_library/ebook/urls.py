from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload_book/', views.upload_book, name='upload_book'),
    path('', views.book_list, name='book_list'),
    path('delete/<int:id>', views.delete_book, name='delete_book'),
    path('user_profile/<str:username>', views.get_user_profile, name='user_profile'),
    path('search', views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
