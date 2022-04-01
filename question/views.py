from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView

from . import models
from . import forms


# Create your views here.


def question_today(request):
    question_of_the_day = models.Question.objects.all().last()
    if request.user.is_authenticated:
        if request.method == 'POST':
            answer_form = forms.AnswerForm(request.POST)
            if answer_form.is_valid():
                new_answer = answer_form.save(commit=False)
                new_answer.question = question_of_the_day
                new_answer.author = request.user
                new_answer.save()
                return redirect(question_of_the_day)
        else:
            answer_form = forms.AnswerForm()
        return render(request, 'question/question_today.html',
                      {'question_today': question_of_the_day,
                       'answer_form': answer_form})
    else:
        unregistered = 'Чтобы ответить, войдите в свой профиль или зарегистрируйтесь.'
        return render(request, 'question/question_today.html',
                      {'question_today': question_of_the_day,
                       'unregistered': unregistered})


# def all_questions(request):
# questions = models.Question.objects.all()[::-1]
# return render(request, 'question/all_questions.html',
# {'questions': questions})


class QuestionListView(ListView):
    queryset = models.Question.objects.all()[::-1]
    context_object_name = 'questions'
    template_name = 'question/all_questions.html'


def discussion_question(request, slug):
    every_question = get_object_or_404(models.Question, slug=slug)
    answers = models.Answer.objects.filter(question=every_question)
    return render(request, "question/discussion_question.html",
                  {"every_question": every_question,
                   'answers': answers})


def custom_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('user was logged in')
                else:
                    return HttpResponse('user account is not activated')
            else:
                return HttpResponse('Incorrect User/Password')
    else:
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})


def view_profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == "POST":
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user, photo="unknown.jpg")
            return render(request, 'registration/registration_complete.html',
                          {'new_user': new_user})
        else:
            return HttpResponse('bad credentials')
    else:
        user_form = forms.RegistrationForm(request.POST)
        return render(request, 'registration/register_user.html', {"form": user_form})


def _get_forms(request, post_method):
    user_form = forms.UserEditForm(request.POST, instance=request.user)
    kw = {'instance': request.user.profile}
    if post_method:
        kw.update({'files': request.FILES})
    profile_form = forms.ProfileEditForm(request.POST, **kw)
    return user_form, profile_form


def edit_profile(request):
    post_method = request.method == "POST"
    user_form, profile_form = _get_forms(request, post_method)
    if post_method:
        if profile_form.is_valid():
            if user_form.is_valid():
                if not profile_form.cleaned_data['photo']:
                    profile_form.cleaned_data['photo'] = request.user.profile.photo
                profile_form.save()
                user_form.save()
                return render(request, 'profile.html')
    else:
        return render(request,
                      'edit_profile.html',
                      {'user_form': user_form, 'profile_form': profile_form})
