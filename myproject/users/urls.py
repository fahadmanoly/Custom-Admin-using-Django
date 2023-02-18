
from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('', views.user_login, name='login'),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
