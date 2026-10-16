from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Feedback  
from .services import chamar_claude, gerar_resposta_brian
import json
from django.http import JsonResponse

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

# Removido o @login_required para permitir acesso público ao testar e estilizar
def index(request):
    return render(request, 'forum/index.html')

def sobre_nos(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        if mensagem:
            user = request.user if request.user.is_authenticated else None
            Feedback.objects.create(usuario=user, mensagem=mensagem)
            return redirect('sobre_nos')
            
    feedbacks = Feedback.objects.all().order_by('-data_criacao')
    return render(request, 'forum/sobre_nos.html', {'feedbacks': feedbacks})

def sobre_empresa(request):
    return render(request, 'forum/sobre_empresa.html')

def ia_chat(request):
    # Se a requisição vier do JavaScript (fetch via POST)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            
            # Processa a mensagem usando o Brian / Claude
            resposta_ia = gerar_resposta_brian(user_message) 
            
            return JsonResponse({"reply": resposta_ia})
        except Exception as e:
            return JsonResponse({"reply": f"Erro interno: {str(e)}"}, status=500)

    # Se for GET, apenas renderiza a página do chat
    return render(request, 'forum/ia_chat.html')