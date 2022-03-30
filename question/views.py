from django.shortcuts import render
from . import models
from datetime import date

# Create your views here.


def question_today(request):
    question_of_the_day = models.Question.objects.all().last()
    return render(request, 'question/question_today.html',
                  {'question_today': question_of_the_day})

def all_questions(request):
    questions = models.Question.objects.all()[::-1]
    return render(request, 'question/all_questions.html',
                  {'questions': questions})


