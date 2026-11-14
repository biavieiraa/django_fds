from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from .models import Feedback, Conversa, Mensagem, QuizResultado
from .services import chamar_claude, gerar_resposta_brian, ErroBrian
from .quiz import PERGUNTAS, PERGUNTAS_CONTEXTO, PERFIS_INFO, calcular_perfil, limpar_texto
from django.db import IntegrityError


def register(request):
    error = None
    if request.method == 'POST':
        usuario = (request.POST.get('username') or '').strip()
        senha = request.POST.get('password')

        if not usuario or not senha:
            error = 'Preencha o usuário e a senha!'
        elif User.objects.filter(username=usuario).exists():
            error = 'Este usuário já existe!'
        else:
            try:
                user = User.objects.create_user(username=usuario, password=senha)
            except IntegrityError:
                error = 'Este usuário já existe!'
            else:
                login(request, user)
                return redirect('ia_chat')

    return render(request, 'forum/register.html', {'error': error})

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

def _perfil_atual(request):
    """Perfil do quiz: último resultado no banco (logado) ou na sessão (visitante)."""
    if request.user.is_authenticated:
        ultimo = QuizResultado.objects.filter(usuario=request.user).first()
        if ultimo:
            return ultimo.perfil
    return request.session.get("quiz_perfil")

def _contexto_atual(request):
    """Respostas de contexto (área da empresa etc.): banco (logado) ou sessão (visitante)."""
    if request.user.is_authenticated:
        ultimo = QuizResultado.objects.filter(usuario=request.user).first()
        if ultimo:
            return ultimo.contexto or {}
    return request.session.get("quiz_contexto") or {}

def _respostas_atual(request):
    """Respostas das perguntas pontuadas: banco (logado) ou sessão (visitante)."""
    if request.user.is_authenticated:
        ultimo = QuizResultado.objects.filter(usuario=request.user).first()
        if ultimo:
            return ultimo.respostas or {}
    return request.session.get("quiz_respostas") or {}


def _resumo_quiz(request):
    """Monta o texto 'Resultado do quiz' que vai para o Brian."""
    perfil = _perfil_atual(request)
    if not perfil:
        return ""

    contexto = _contexto_atual(request)
    respostas = _respostas_atual(request)
    linhas = ["Resultado do quiz:"]
    numero = 1

    for c in PERGUNTAS_CONTEXTO:
        if c["id"] in contexto:
            linhas.append(f"{numero}. {c['texto']} Resposta: {contexto[c['id']]}")
        numero += 1

    for p in PERGUNTAS:
        if p["id"] in respostas:
            linhas.append(f"{numero}. {p['texto']} Resposta: {respostas[p['id']]}")
        numero += 1

    titulo = PERFIS_INFO.get(perfil, {}).get("titulo", perfil)
    linhas.append(f"Perfil calculado: {titulo}")
    return "\n".join(linhas)


def _contexto_para_template():
    return [
        {
            "id": c["id"],
            "texto": c["texto"],
            "opcoes": c["opcoes"],
            "permite_outro": c.get("permite_outro", False),
        }
        for c in PERGUNTAS_CONTEXTO
    ]

def _perguntas_para_template():
    return [
        {
            "id": p["id"],
            "texto": p["texto"],
            "opcoes": [{"valor": i, "texto": texto} for i, (texto, _) in enumerate(p["opcoes"])],
        }
        for p in PERGUNTAS
    ]


def quiz(request):
    contexto = {"perguntas": _perguntas_para_template()}

    if request.method == "POST":
        total = 0
        for p in PERGUNTAS:
            try:
                total += p["opcoes"][int(request.POST.get(p["id"]))][1]
            except (TypeError, ValueError, IndexError):
                contexto["error"] = "Responda todas as perguntas para ver seu resultado."
                return render(request, "forum/quiz.html", contexto)

        perfil = calcular_perfil(total)
        request.session["quiz_perfil"] = perfil
        if request.user.is_authenticated:
            QuizResultado.objects.create(usuario=request.user, pontuacao=total, perfil=perfil)

        contexto["resultado"] = {"perfil": perfil, **PERFIS_INFO[perfil]}

    return render(request, "forum/quiz.html", contexto)


@require_POST
def quiz_enviar(request):
    total = 0
    respostas = {}
    for p in PERGUNTAS:
        try:
            texto_opcao, pontos = p["opcoes"][int(request.POST.get(p["id"]))]
        except (TypeError, ValueError, IndexError):
            return JsonResponse({"erro": "Responda todas as perguntas."}, status=400)
        total += pontos
        respostas[p["id"]] = texto_opcao

    contexto = {}
    for c in PERGUNTAS_CONTEXTO:
        resposta = limpar_texto(request.POST.get(c["id"]))
        if resposta:
            contexto[c["id"]] = resposta

    perfil = calcular_perfil(total)
    request.session["quiz_perfil"] = perfil
    request.session["quiz_contexto"] = contexto
    request.session["quiz_respostas"] = respostas

    if not request.session.session_key:
        request.session.save()

    QuizResultado.objects.create(
        usuario=request.user if request.user.is_authenticated else None,
        sessao=request.session.session_key or "",
        pontuacao=total,
        perfil=perfil,
        contexto=contexto,
        respostas=respostas,
    )

    return JsonResponse({"perfil": perfil, **PERFIS_INFO[perfil]})


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
            resposta = chamar_claude(
                user_message, arquivo, historico,
                _perfil_atual(request), _contexto_atual(request), _respostas_atual(request)
            )
        except ErroBrian as e:
            return JsonResponse({"reply": str(e)})  # erro não vai pro histórico
        except Exception as e:
            return JsonResponse({"reply": f"Erro interno: {str(e)}"}, status=500)

        criada = False
        if conversa is None:
            conversa = Conversa.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                titulo=(user_message or "Arquivo enviado")[:60],
            )
            request.session["conversa_id"] = conversa.id
            criada = True

        texto_usuario = user_message
        if arquivo:
            texto_usuario = f"[Arquivo anexado: {arquivo.name}]\n{user_message}".strip()

        Mensagem.objects.create(conversa=conversa, papel="user", texto=texto_usuario)
        Mensagem.objects.create(conversa=conversa, papel="assistant", texto=resposta)
        conversa.save(update_fields=["atualizada_em"])

        return JsonResponse({"reply": resposta, "nova_conversa": criada})

    # GET: renderiza a página com o histórico e a barra lateral
    conversa = _conversa_ativa(request)
    mensagens = conversa.mensagens.all() if conversa else []
    conversas = (
        Conversa.objects.filter(usuario=request.user).order_by("-atualizada_em")
        if request.user.is_authenticated else []
    )
    perfil = _perfil_atual(request)
    return render(request, "forum/ia_chat.html", {
        "mensagens": mensagens,
        "conversas": conversas,
        "conversa_atual_id": conversa.id if conversa else None,
        "perfil": perfil,
        "perfil_titulo": PERFIS_INFO.get(perfil, {}).get("titulo"),
        "perguntas": _perguntas_para_template(),
        "iniciar_quiz": perfil is None and not mensagens,
        "perguntas_contexto": _contexto_para_template(),
    })


@require_POST
def nova_conversa(request):
    request.session["conversa_id"] = None
    return redirect("ia_chat")


@login_required(login_url="login")
def abrir_conversa(request, conversa_id):
    conversa = get_object_or_404(Conversa, id=conversa_id, usuario=request.user)
    request.session["conversa_id"] = conversa.id
    return redirect("ia_chat")


@require_POST
@login_required(login_url="login")
def apagar_conversa(request, conversa_id):
    conversa = get_object_or_404(Conversa, id=conversa_id, usuario=request.user)
    if request.session.get("conversa_id") == conversa.id:
        request.session["conversa_id"] = None
    conversa.delete()
    return redirect("ia_chat")