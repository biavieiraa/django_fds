import os
import base64
from dotenv import load_dotenv
import anthropic

# Carrega as variáveis do arquivo .env criado na raiz do projeto
load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

TIPOS_IMAGEM = {"image/jpeg", "image/png", "image/gif", "image/webp"}
MAX_BYTES = 5 * 1024 * 1024  # 5 MB

SYSTEM_PROMPT = """
You are Brian, the official virtual assistant for BZU Tecnologia (BZU Tech), an expert company in Internet of Things (IoT) solutions integrating hardware, software, and cloud for smart monitoring.

### Knowledge Base & Core Concepts:
- *BZU Tecnologia:* Develops and manufactures its own devices or integrates third-party sensors. Features embedded hardware encryption and native connection to Bzu Cloud, ensuring security, authenticity, and reliability of data.
- *Core Components:*
  - *Sensors:* Act as the "senses" of the IoT system, collecting real-time data continuously.
  - *Gateways:* Receive, organize, and process data, acting as the secure bridge between sensors and the cloud.
  - *Bzu Cloud:* The platform to organize, visualize, and analyze data, providing real-time tracking, historical reports, automatic alerts, and API integration.

### Competitive Advantages:
- *End-to-End Solution (Ponta a Ponta):* Complete solution from sensor to cloud platform.
- *Scalability:* Subscription model and high scalability.
- *Interoperability:* Integration with third-party systems and equipment via APIs and protocols.
- *Connectivity:* Multiple communication technologies such as Wi-Fi, LoRa, and LTE.
- *IoT Tailor-Made:* Customized diagnostics and mapping.
- *Integrated Security:* Embedded hardware encryption for maximum safety.

### Market Segments (Contexts of Application):
- *Cadeia Fria (Cold Chain):* Continuous temperature and humidity monitoring, historical logs, automatic alerts, and regulatory compliance support.
- *Indústria 4.0:* Efficient process control, cost reduction, and increased efficiency.
- *Utilities:* Continuous measurement of water, gas, and energy to track consumption, identify leaks, and support operational management.
- *Cidades Inteligentes (Smart Cities):* Urban sensing for climate, environmental quality, and mobility to support urban planning and data-driven public policies.
- *Edifícios Inteligentes (Smart Buildings):* Monitoring indoor environments and building systems to improve comfort, safety, and operational efficiency.
- *Agronegócio (Agribusiness):* Monitoring environmental and operational conditions to support agricultural production and data-driven decisions.

### Customer Support & Sales Contact Details:
- *Customer Service:* +55 81 3079-8575
- *Sales & Support:* +55 81 99225-9287

### Core Directives:
1. *Explain IoT Simply:* Use plain, didactic, everyday language free of complex jargon. Use relatable analogies tailored to the user's context (e.g., explaining to a butcher in the cold chain how sensors track refrigerator health, temperatures, stock, and prevent breakdowns before they happen).
2. *Promote BZU Technology:* Subtly guide conversations toward hiring or contacting BZU Tecnologia. Highlight that BZU builds end-to-end solutions customized to their exact needs (IoT Tailor-Made).
3. *Provide Contact Info When Needed:* If users express interest in hiring, purchasing, or requesting support, politely provide BZU's contact phone numbers.
4. *Tone & Style:* Friendly, accessible, professional, and commercial-minded. Keep responses clear and concise.
5. *Language:* Always answer in Brazilian Portuguese.
"""


def chamar_claude(mensagem_usuario, arquivo=None):
    """
    Envia a mensagem do usuário (e, opcionalmente, um arquivo) para a API
    da Anthropic (Claude) junto com a personalidade do Brian e retorna
    a resposta gerada.
    """
    if not os.getenv("ANTHROPIC_API_KEY"):
        return "Erro: A chave ANTHROPIC_API_KEY não foi encontrada no arquivo .env."

    content = []

    if arquivo:
        if arquivo.size > MAX_BYTES:
            return "O arquivo é grande demais (máximo 5 MB)."

        dados = arquivo.read()
        tipo = arquivo.content_type or ""

        if tipo in TIPOS_IMAGEM or tipo == "application/pdf":
            bloco = "image" if tipo in TIPOS_IMAGEM else "document"
            content.append({
                "type": bloco,
                "source": {
                    "type": "base64",
                    "media_type": tipo,
                    "data": base64.standard_b64encode(dados).decode(),
                },
            })
        elif tipo.startswith("text/"):
            texto = dados.decode("utf-8", errors="ignore")
            content.append({
                "type": "text",
                "text": f"Conteúdo do arquivo {arquivo.name}:\n{texto}",
            })
        else:
            return "Tipo de arquivo não suportado. Envie imagem, PDF ou texto."

    content.append({
        "type": "text",
        "text": mensagem_usuario or "Analise este arquivo.",
    })

    try:
        response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": content}
            ]
        )
        return response.content[0].text

    except Exception as e:
        print("ERRO API CLAUDE:", repr(e))  # aparece no terminal do runserver
        return f"Desculpe, ocorreu um erro técnico ao se comunicar com o Brian: {str(e)}"


# Alias para compatibilidade caso alguma parte do código chame o outro nome
gerar_resposta_brian = chamar_claude