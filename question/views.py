from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from . import models, forms
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.


def question_today(request):
    question_of_the_day = models.Question.objects.all().last()
    return render(request, 'question/question_today.html',
                  {'question_today': question_of_the_day})


def all_questions(request):
    questions = models.Question.objects.all()[::-1]
    return render(request, 'question/all_questions.html',
                  {'questions': questions})


def discussion_question(request, slug):
    every_question = get_object_or_404(models.Question, slug=slug)
    return render(request, "question/discussion_question.html",
                  {"every_question": every_question})


def send_answer(request, question_id):
    question = get_object_or_404(models.Answer,
                                 id=question_id)
    if request.method == 'POST':
        answer_form = forms.AnswerForm(request.POST)
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.question = question.question
            new_answer.author = User.objects.first()     #нужно выбрать текущего пользователя
            new_answer.publish = timezone.now()
            new_answer.save()
    else:
        answer_form = forms.AnswerForm()
    return render(request,
                  "question/question_today.html",
                  {'answer_form': answer_form})


def suggest_question(request):
    if request.method == 'POST':
        question_form = forms.QuestionForm(request.POST)
        if question_form.is_valid():
            cd = question_form.cleaned_data
            subject = 'Suggest question'
            author = User.objects.first()
            suggest = cd['suggest_question']
            body = (f'Author of question: {author}\n{suggest}')
            send_mail(subject, body, 'user@mu.com', ('admin@mu.com',))

    else:
        question_form = forms.QuestionForm()
    return render(request, 'question/question_today.html',
                  {'question_form': question_form})
