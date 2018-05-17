from django.contrib import admin
from django.urls import path, include
from .views import home, login, register

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register')
]
