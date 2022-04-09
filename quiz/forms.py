from django import forms
from django.contrib.auth.models import User
from .models import Quiz, Submission, UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = "__all__"

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             "password": forms.PasswordInput
#         }
