from django import forms
from . import models
from django.contrib.auth.models import User


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ('comment', )


class QuestionForm(forms.Form):
    suggest_question = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password2']
