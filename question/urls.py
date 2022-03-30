from django.urls import path
from . import views

app_name = 'question'
urlpatterns = [
    path('', views.question_today, name='question_today'),
    path('all-questions/', views.all_questions, name='all_questions'),
    path('<slug:slug>/', views.discussion_question,
         name='discussion_question'),
]
