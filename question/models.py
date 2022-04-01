from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.

class Question(models.Model):
    main_question = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255)
    publish_question = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='user_delete')

    def get_absolute_url(self):
        return reverse('question:discussion_question',
                       args=[self.slug, ])


class Answer(models.Model):
    comment = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_answer')
    publish = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    pass
