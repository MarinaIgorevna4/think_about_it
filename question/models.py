from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    main_question = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255)
    publish_question = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='user_delete')
