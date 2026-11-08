PERGUNTAS = [
    {
        "id": "q1",
        "texto": "Você já ouviu falar em Internet das Coisas (IoT)?",
        "opcoes": [
            ("Nunca ouvi falar", 0),
            ("Já ouvi o termo, mas não sei explicar", 1),
            ("Sei explicar mais ou menos o que é", 2),
            ("Conheço bem e consigo explicar para outras pessoas", 3),
        ],
    },
    {
        "id": "q2",
        "texto": "Você usa algum dispositivo conectado à internet que coleta dados ou é controlado à distância (câmera, lâmpada inteligente, sensor, relógio inteligente)?",
        "opcoes": [
            ("Não uso nenhum", 0),
            ("Tenho algum, mas uso só o básico", 1),
            ("Uso alguns com frequência", 2),
            ("Uso vários e já fiz eles trabalharem juntos", 3),
        ],
    },
    {
        "id": "q3",
        "texto": "Você sabe o que é um sensor e como ele envia informações?",
        "opcoes": [
            ("Não sei", 0),
            ("Tenho uma ideia vaga", 1),
            ("Sei o básico", 2),
            ("Conheço tipos de sensores, gateways e conectividade (Wi-Fi, LoRa, LTE)", 3),
        ],
    },
    {
        "id": "q4",
        "texto": "No seu trabalho ou negócio, algo é monitorado automaticamente (temperatura, consumo de energia, estoque)?",
        "opcoes": [
            ("Não, tudo é feito na mão", 0),
            ("Monitoro manualmente, com anotações ou planilhas", 1),
            ("Temos alguns equipamentos que monitoram", 2),
            ("Temos monitoramento automático com alertas e relatórios", 3),
        ],
    },
    {
        "id": "q5",
        "texto": "Você já pensou em implementar ou contratar uma solução de IoT?",
        "opcoes": [
            ("Nunca pensei nisso", 0),
            ("Já pensei, mas nunca pesquisei", 1),
            ("Já pesquisei ou pedi orçamento", 2),
            ("Já implementei ou contratei", 3),
        ],
    },
    {
        "id": "q6",
        "texto": "Você já trabalhou com dados vindos de dispositivos (gráficos, relatórios, integrações)?",
        "opcoes": [
            ("Nunca", 0),
            ("Só vi gráficos prontos", 1),
            ("Já analisei dados e relatórios", 2),
            ("Já integrei dados por API ou programei algo", 3),
        ],
    },
]

PONTUACAO_MAXIMA = len(PERGUNTAS) * 3

PERFIS_INFO = {
    "iniciante": {
        "titulo": "Explorador",
        "descricao": "Você está começando agora, e tudo bem! O BrIAn vai explicar IoT do zero, com exemplos do dia a dia.",
    },
    "curioso": {
        "titulo": "Curioso",
        "descricao": "Você já conhece o assunto, mas ainda não usa. O BrIAn vai mostrar como começar e quais benefícios esperar.",
    },
    "usuario": {
        "titulo": "Usuário de IoT",
        "descricao": "Você já tem experiência. O BrIAn vai conversar de forma mais técnica e falar de expansão e integração.",
    },
}


def calcular_perfil(pontos):
    if pontos * 3 <= PONTUACAO_MAXIMA:
        return "iniciante"
    if pontos * 3 <= PONTUACAO_MAXIMA * 2:
        return "curioso"
    return "usuario"