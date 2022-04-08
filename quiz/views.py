from django.shortcuts import render, HttpResponse
from .forms import AddQuestionForm
from .models import Quiz, Submission
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from rest_framework.viewsets import ModelViewSet
from .serializer import QuizSerializer
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

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
        for que, ans in request.POST.items():
            if que == 'csrfmiddlewaretoken':
                continue
            print('que', que)
            q_obj = Quiz.objects.get(question=que)
            is_correct = True if ans == q_obj.answer else False
            Submission.objects.create(q_id=q_obj, user_id=request.user, sub_answer=q_obj, is_correct=is_correct)
        return render(request, 'quiz/results.html', {})
    # if request.user.is_authenticated:
    #     return render(request, 'quiz/home.html')
    # else:
    #     return redirect('login')
def report_page(request, internal=False):
    resp = Submission.objects.filter(user_id=request.user)
    scores = 0
    wrong = 0
    correct = 0
    total = 0
    for r in resp:
        total += 1
        if r.is_correct:
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
    if internal:
        return responses
    return render(request, 'quiz/results.html', context=responses)

def report_mailer(request):
    subject = "Report Mailer"
    resp = report_page(request, True)
    msg = f"""
        <html><body>
        <h1> Welcome to Credo Quiz </h1>
        <h2> Hi! { request.user }</h2>
        <h3> Your Result! </h3>
        <h4> Wrong Answers   - { resp['wrong'] } </h4>
        <h4> Correct Answers - { resp['correct'] } </h4>
        <h4> Answered        - { resp['total'] } / 20 </h4>
        <h4> Total Scores    - { resp['scores'] } / 100 </h4>
        </body></html>
    """
    print('resp', subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    # out = send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    out = EmailMessage(subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    out.content_subtype = "html"
    out.send()
    print('email out', out)
    return redirect(resolve_url('report'))
    
def quiz_page(request):
    form_data = AddQuestionForm()
    return render(request, 'quiz/index.html', {'form': form_data})

# Rest Framework Views
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

