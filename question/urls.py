from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'question'
urlpatterns = [
    path('', views.question_today, name='question_today'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.custom_login, name='login'),
    # path('all-questions/', views.all_questions, name='all_questions'),
    path('all-questions/', views.QuestionListView.as_view(), name='all_questions'),
    path('<slug:slug>/', views.discussion_question, name='discussion_question'),
]
