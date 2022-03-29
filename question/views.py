from django.shortcuts import render
from . import models

# Create your views here.

def all_questions(request):
    questions = models.Question.objects.all()
    return render(request, 'question/all_questions.html',
                  {'questions': questions})
