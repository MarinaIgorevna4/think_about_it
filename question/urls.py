from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static


app_name = 'question'


class MyHuck(auth_views.PasswordResetView):
    success_url = reverse_lazy("question:password_reset_done")


urlpatterns = [
    path('question/', views.question_today, name='question_today'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.custom_login, name='login'),
    # path('all-questions/', views.all_questions, name='all_questions'),
    path('all-questions/', views.QuestionListView.as_view(), name='all_questions'),
    path("password_reset/", MyHuck.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("question:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('profile/', views.view_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('<slug:slug>/', views.discussion_question, name='discussion_question'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

