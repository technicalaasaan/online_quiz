from django.shortcuts import render, HttpResponse
from .forms import AddQuestionForm
from .models import Quiz
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.viewsets import ModelViewSet
from .serializer import QuizSerializer

# Create your views here.
def login_page(request):
    if request.method == "POST":
        print('am here')
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print('un', uname, pwd)
        user_data = authenticate(request, username=uname, password=pwd)
        print('user', user_data)
        if user_data:
            login(request, user_data)
            return redirect('/')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        if pwd1 != pwd2:
            return HttpResponse('Invalid Password', status=400)
        if User.objects.filter(username=uname):
            return HttpResponse('Username Exist', status=400)
        user_data = User.objects.create(
            username = uname,
            email = email,
            password = pwd1
        )
        if user_data:
            login(request, user_data)
            return redirect('/')
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def home(request):
    questions = Quiz.objects.all()
    if request.method == "GET":        
        return render(request, 'quiz/home.html', {'questions': questions})
    else:
        scores = 0
        wrong = 0
        correct = 0
        total = 0
        print(request.POST)
        for q in questions:
            if q.question in request.POST:
                total += 1
                if q.answer == request.POST.get(q.question):
                    scores += 5
                    correct += 1
                else:
                    wrong += 1        
        responses = {
            "scores": scores,
            "wrong": wrong,
            "correct": correct,
            "total": total
        }            
        return render(request, 'quiz/results.html', responses)
    # if request.user.is_authenticated:
    #     return render(request, 'quiz/home.html')
    # else:
    #     return redirect('login')

def quiz_page(request):
    form_data = AddQuestionForm()
    return render(request, 'quiz/index.html', {'form': form_data})

# Rest Framework Views
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

