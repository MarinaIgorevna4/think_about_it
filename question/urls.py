from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'question'
urlpatterns = [
    path('', views.question_today, name='question_today'),
    path('all-questions/', views.all_questions, name='all_questions'),
]
