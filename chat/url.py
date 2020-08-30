from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('sign-in/', views.sign_in, name='login'),
    path('sign-up/', views.sign_up, name='register'),
    path('chat/', views.chat, name='chat'),
]
