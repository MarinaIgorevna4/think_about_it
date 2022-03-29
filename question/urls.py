from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'question'
urlpatterns = [
    path('', views.all_questions, name='all_questions'),
]
