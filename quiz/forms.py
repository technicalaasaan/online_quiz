from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Quiz


class AddQuestionForm(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"
