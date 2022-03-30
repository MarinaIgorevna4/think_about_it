from django import forms
from . import models


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ('comment', )


class QuestionForm(forms.Form):
    suggest_question = forms.CharField(widget=forms.Textarea)
