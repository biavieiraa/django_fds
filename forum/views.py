from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from .models import Feedback, Conversa, Mensagem
from .services import chamar_claude, gerar_resposta_brian, ErroBrian


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


LIMITE_HISTORICO = 20  

def _conversa_ativa(request):
    """Devolve a conversa da sessão (ou None), garantindo que é do dono certo."""
    if "conversa_id" not in request.session:
        if request.user.is_authenticated:
            ultima = (Conversa.objects.filter(usuario=request.user)
                      .order_by("-atualizada_em").first())
            request.session["conversa_id"] = ultima.id if ultima else None
            return ultima
        return None

    conversa_id = request.session["conversa_id"]
    if not conversa_id:
        return None

    conversa = Conversa.objects.filter(id=conversa_id).first()
    if conversa is None:
        return None

    if request.user.is_authenticated:
        if conversa.usuario_id is None:
            conversa.usuario = request.user
            conversa.save(update_fields=["usuario"])
        elif conversa.usuario_id != request.user.id:
            return None
    elif conversa.usuario_id is not None:
        return None

    return conversa


@csrf_protect
def ia_chat(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        arquivo = request.FILES.get("arquivo")

        if not user_message and not arquivo:
            return JsonResponse({"reply": "Envie uma mensagem ou um arquivo."})

        conversa = _conversa_ativa(request)
        historico = []
        if conversa:
            ultimas = list(conversa.mensagens.order_by("-id")[:LIMITE_HISTORICO])
            ultimas.reverse()
            historico = [{"role": m.papel, "content": m.texto} for m in ultimas]
            while historico and historico[0]["role"] != "user":
                historico.pop(0)  # a API exige começar por "user"

        try:
            resposta = chamar_claude(user_message, arquivo, historico)
        except ErroBrian as e:
            return JsonResponse({"reply": str(e)})  # erro não vai pro histórico
        except Exception as e:
            return JsonResponse({"reply": f"Erro interno: {str(e)}"}, status=500)

        if conversa is None:
            conversa = Conversa.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                titulo=(user_message or "Arquivo enviado")[:60],
            )
            request.session["conversa_id"] = conversa.id

        texto_usuario = user_message
        if arquivo:
            texto_usuario = f"[Arquivo anexado: {arquivo.name}]\n{user_message}".strip()

        Mensagem.objects.create(conversa=conversa, papel="user", texto=texto_usuario)
        Mensagem.objects.create(conversa=conversa, papel="assistant", texto=resposta)
        conversa.save(update_fields=["atualizada_em"])

        return JsonResponse({"reply": resposta})

    conversa = _conversa_ativa(request)
    mensagens = conversa.mensagens.all() if conversa else []
    return render(request, "forum/ia_chat.html", {"mensagens": mensagens})


@require_POST
def nova_conversa(request):
    request.session["conversa_id"] = None
    return redirect("ia_chat")