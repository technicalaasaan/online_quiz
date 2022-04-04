from django.shortcuts import render
from .forms import AddQuestionForm
from .models import Quiz
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import QuizSerializer

# Create your views here.
def quiz_page(request):
    form_data = AddQuestionForm()
    return render(request, 'quiz/index.html', {'form': form_data})

# Rest Framework Views
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

