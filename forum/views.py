from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Feedback  
from django.shortcuts import render
from .services import chamar_claude
from .services import gerar_resposta_brian
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
            # Se o utilizador estiver autenticado usa request.user, caso contrário guarda como None ou anónimo
            user = request.user if request.user.is_authenticated else None
            Feedback.objects.create(usuario=user, mensagem=mensagem)
            return redirect('sobre_nos')
            
    feedbacks = Feedback.objects.all().order_by('-data_criacao')
    return render(request, 'forum/sobre_nos.html', {'feedbacks': feedbacks})

def sobre_empresa(request):
    return render(request, 'forum/sobre_empresa.html')

def ia_chat(request):
    resposta_ia = None
    prompt_usuario = ""

    if request.method == "POST":
        prompt_usuario = request.POST.get("prompt", "")
        if prompt_usuario:
            resposta_ia = chamar_claude(prompt_usuario)

    return render(request, "forum/ia_chat.html", {
        "resposta": resposta_ia,
        "prompt": prompt_usuario
    })

def ia_chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            
            # Aqui é onde o Brian processa a mensagem usando a API Key e o system prompt
            resposta_ia = gerar_resposta_brian(user_message) 
            
            return JsonResponse({"reply": resposta_ia})
        except Exception as e:
            return JsonResponse({"reply": f"Erro interno: {str(e)}"}, status=500)

    return render(request, 'forum/ia_chat.html')