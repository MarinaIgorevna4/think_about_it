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


def suggest_question(request):
    if request.method == 'POST':
        question_form = forms.QuestionForm(request.POST)
        if question_form.is_valid():
            cd = question_form.cleaned_data
            subject = 'Suggest question'
            author = User.objects.first()
            suggest = cd['suggest_question']
            body = f'Author of question: {author}\n{suggest}'
            send_mail(subject, body, 'user@mu.com', ('admin@mu.com',))

    else:
        question_form = forms.QuestionForm()
    return render(request, 'question/question_today.html',
                  {'question_form': question_form})


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
