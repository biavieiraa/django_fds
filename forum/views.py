from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Feedback
from .services import chamar_claude, gerar_resposta_brian


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


@csrf_protect
def ia_chat(request):
    # POST vindo do JavaScript (fetch com FormData: texto + arquivo opcional)
    if request.method == "POST":
        try:
            user_message = request.POST.get("message", "").strip()
            arquivo = request.FILES.get("arquivo")

            if not user_message and not arquivo:
                return JsonResponse({"reply": "Envie uma mensagem ou um arquivo."})

            resposta_ia = chamar_claude(user_message, arquivo)
            return JsonResponse({"reply": resposta_ia})
        except Exception as e:
            return JsonResponse({"reply": f"Erro interno: {str(e)}"}, status=500)

    # GET: apenas renderiza a página do chat
    return render(request, 'forum/ia_chat.html')