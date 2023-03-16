from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


from . import views

app_name = 'Authentication'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login_page/', views.Login_page, name='login_page' ),
    path('user-login/', views.User_login, name='User_login'),
    path('logout/', views.User_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
