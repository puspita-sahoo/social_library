from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.sign_up, name ='sign_up'),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('user_login/', views.user_login, name ='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
