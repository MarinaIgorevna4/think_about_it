from django.shortcuts import render
from django.shortcuts import get_object_or_404
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


def discussion_question(request, slug, id):
    every_question = get_object_or_404(models.Question,
                                       slug=slug,
                                       id=id)
    return render(request, "question/discussion_question.html",
                  {"every_question": every_question})
