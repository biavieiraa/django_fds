from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Feedback  

def register(request):
    error = None
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        
        if User.objects.filter(username=usuario).exists():
            error = 'Este usuário já existe!'
        elif not usuario or not senha:
            error = 'Preencha o usuário e a senha!'
        else:
            user = User.objects.create_user(username=usuario, password=senha)
            login(request, user)
            return redirect('index')
            
    return render(request, 'forum/register.html', {'error': error})

@login_required
def index(request):
    return render(request, 'forum/index.html')

@login_required
def sobre_nos(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        if mensagem:
            Feedback.objects.create(usuario=request.user, mensagem=mensagem)
            return redirect('sobre_nos')
            
    feedbacks = Feedback.objects.all().order_by('-data_criacao')
    return render(request, 'forum/sobre_nos.html', {'feedbacks': feedbacks})

@login_required
def sobre_empresa(request):
    return render(request, 'forum/sobre_empresa.html')