from django import forms
from django.contrib.auth.models import User
from .models import Quiz


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "password": forms.PasswordInput
        }
