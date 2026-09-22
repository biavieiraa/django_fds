# Análise de Competidores

## Empresa analisada - TIM IoT solutions

### Visão geral

A tim Iot solutions é um portfólio corporativo de internet das coisas da operadora TIM, construído sobre infraestrutura de conectividade da empresa. Seu público alvo são empresas de médio e grande portes de setores como: agronegócio, indúnstria e lógistica.

### Produtos analisados

- TIM IoT plataform: plataforma de gestão de dispositivos Iot que conecta, monitora e automatiza processos
- Smart metering: telemetria para monitoramento remoto de água e gás, votada a concessionárias, shoppins e aeroportos
- Smart Lighting: telegestão de iluminação pública via rede NB-IoT, já usada em milhares de pontos de iluminação no Brasil.
- Chip M2M / TIM Data: conectividade M2M (machine-to-machine) usada como base para rastreamento, telemetria e sensores.

### Funcionamento

1. Conectividade: o dispositivo do cliente (sensor, medidor, luminária, rastreador) se conecta à rede da TIM via NB-IoT, Cat-1, 4G ou 5G — tecnologias otimizadas para baixo consumo de energia e longo alcance.
2. Ingestão de dados: os dados coletados trafegam pela rede da operadora até a TIM IoT Platform, que consolida as informações vindas de diferentes máquinas, sensores ou equipamentos.
3. Gestão e integração: a plataforma permite dashboards customizados, cálculo de KPIs e integração direta com sistemas corporativos (ERP, MES, bancos de dados e nuvens externas) via APIs padrão como MQTT e HTTP.
4. Aplicação especializada (principal diferencial): dependendo do segmento, a TIM oferece camadas prontas sobre essa base — por exemplo, o Smart Metering já entrega alertas de vazamento e falhas com bateria de até 10 anos, e o Smart Lighting já entrega dimerização inteligente e tarifação por consumo real.

**RESUMO:** De forma Geral, a TIM entrega principalmente a conectividade confiável em escala nacional e uma camada de plataforma/aplicação por cima, enquanto o hardware de ponta costuma vir de parceiros ou do próprio cliente.

### Pontos Fortes

1. Infraestrutura de rede própria e nacional: cobertura 4G/5G/NB-IoT em todo o Brasil, incluindo áreas rurais e remotas, algo que várias empresas não possuem e precisam contratar de terceiros.
2. Escala: histórico de grandes implantações, como mais de 260 mil pontos de iluminação pública conectados, o que comprova capacidade de atender projetos de grande porte
3. Portfólio amplo: soluções prontas para múltiplos setores, com cases e parcerias já consolidadas
4. Marca e força comercial: por ser uma operadora de telecom estabelecida, tem maior força, equipe comercial e vendas B2B do que uma empresa que ainda está crescendo no mercado.

### Pontos fracos

1. Menor especialização em hardware e sensoriamento: a TIM é provedora principalmente de conectividade e plataforma, o desenvolvimento de sensores e dispositivos de ponta frequentemente depende de parceiros terceiros.
2. Soluções padronizadas: por ser uma oferta padronizada em escala nacional, tende a ser menos flexível para diagnósticos e mapeamentos customizados por cliente.
3. Foco em múltiplos setores perdendo especialização: como atende praticamente todos os setores de utilities e indústria, a TIM não tem alto nível de de especialização
4. Atendimento "distante": por ser uma grande empresa de telecom, o atendimento tende a ser menos próximo e consultivo do que o modelo de proximidade que empresas regionais
5. Dependência de parcerias para fechar o sistema completo: a TIM monta seu sistema unindo vários parceiros, o que pode gerar mais camadas de negociação e suporte para o cliente final.

---

## Empresa analisada - Datatem

### Visão geral

A Datatem é uma empresa brasileira especializada em conectividade M2M e IoT. A empresa fornece chips, conectividade e ferramentas de gestão para permitir que máquinas, sensores e dispositivos transmitam dados continuamente pela internet.

Seu público é principalmente empresarial (B2B), especialmente organizações que possuem muitos equipamentos conectados ou operações que dependem de comunicação constante. Entre os setores atendidos se destacam os de: energia, rastreamento, indústria, segurança eletrônica e agricultura.

### Produtos analisados

1. Chip/SIM card M2M e IoT: utilizado para conectar máquinas, sensores, veículos e equipamentos às redes móveis.
2. Conectividade multioperadora: permite utilizar diferentes redes de operadoras e gerenciar as conexões em uma única plataforma.
3. APN privada, VPN e IP fixo: recursos voltados à comunicação mais controlada e segura entre os dispositivos e os sistemas da empresa.

### Funcionamento

O dispositivo conectado coleta os dados e o chip M2M/IoT realiza a comunicação com a rede móvel. Esses dados são transmitidos pela infraestrutura de conectividade e podem ser gerenciados por meio da plataforma da Datatem, que permite monitorar a conectividade, controlar o consumo e acessar informações.

Após a transmissão, os dados podem ser encaminhados aos sistemas da própria organização para armazenamento, processamento, análise e tomada de decisões.

### Pontos fortes

- Conectividade multioperadora, permitindo gerenciar conexões de diferentes redes em uma única plataforma.
- Gestão centralizada de chips, facilitando o acompanhamento de grandes quantidades de dispositivos.
- Recursos de segurança, como APN privada, VPN e IP fixo.
- Ampla aplicação em diferentes setores, como agronegócio, indústria, energia, e rastreamento.
- Integração com soluções IoT, atuando como infraestrutura de comunicação entre dispositivos e sistemas empresariais.

### Pontos fracos

- Não é uma solução completa de análise de dados: seu foco principal é a conectividade e o gerenciamento dos dispositivos. A análise estratégica dos dados pode exigir outros softwares ou plataformas.
- Dependência da cobertura das redes móveis: mesmo com conectividade multioperadora, regiões remotas ou com baixa cobertura podem apresentar limitações.
- Foco empresarial: a solução é direcionada principalmente para empresas que possuem múltiplos dispositivos conectados, não sendo voltada ao usuário comum.
- Maior complexidade técnica: a implantação pode exigir conhecimentos em redes, telecomunicações, IoT, APN, VPN e integração de sistemas.
- O valor depende da aplicação: apenas conectar dispositivos não garante benefícios para a empresa; é necessário definir como os dados serão coletados, armazenados, analisados e utilizados na tomada de decisões

---

## Empresa analisada: IoT Connect

### Visão geral

A IoT Connect atua como uma camada intermediária de conectividade e gestão de ativos. O foco central é simplificar a ponte entre o hardware do chão de fábrica (sensores, gateways e módulos M2M) e as aplicações em nuvem, resolvendo o gargalo de integrar múltiplos protocolos sem reinventar a roda.

### Produtos analisados

Plataforma de Gestão de Conectividade (gestão de chips M2M/eSIM), o Módulo de Gestão de Dispositivos (cadastro e status do hardware), o Motor de Regras e Notificações (alertas automáticos), os Dashboards de Telemetria (visualização em tempo real) e a Camada de Integração via APIs (conexão com Power BI e ERPs).

### Funcionamento

1. Controla a ativação, suspensão e o consumo do tráfego de dados dos chips instalados nos sensores e gateways da fábrica.
2. Centraliza o cadastro via identificadores (IMEI), provisionamento e o acompanhamento do estado de saúde física e operacional do hardware.
3. Processa os dados brutos recebidos dos sensores e dispara ações automáticas (e-mails, SMS) ao identificar divergências nos limites operacionais.
4. Converte a leitura bruta dos sensores em gráficos, medidores e indicadores visuais para acompanhamento da operação no dia a dia.
5. Fornece pontes de comunicação seguras para enviar e receber dados entre a plataforma IoT e sistemas externos como Power BI, ERPs e CRMs.

### Pontos Fortes

1. Monitoramento do consumo de dados em tempo real por dispositivo.
2. Cadastro rápido e em massa via importação de planilhas.
3. Disparo instantâneo de alertas por múltiplos canais.
4. Interface responsiva para acesso por computador, tablet ou celular.
5. Autenticação segura através de tokens e chaves de acesso.

### Pontos Fracos

1. Dependência direta da cobertura das operadoras parceiras no local.
2. Exige parametrização manual demorada para hardwares fora do padrão.
3. Regras encadeadas e lógicas avançadas exigem conhecimento de código.
4. Dificuldade para cruzar dados de múltiplos sensores na mesma tela.
5. Interface nativa ruim para encontrar erros de integração.

---

## Empresa analisada: Claro

### Visão Geral

1. A Claro é uma das maiores empresas de telecomunicações da América Latina, atuando no Brasil como uma operadora multisserviços que oferece soluções conectadas para pessoas físicas, pequenas empresas e corporações. Provedora de serviços integrados de conectividade e entretenimento, oferecendo telefonia móvel (4G e 5G), internet banda larga de alta velocidade (fibra óptica e cabo), TV por assinatura (cabo e via streaming) e telefonia fixa.
2. Público-Alvo: Abrange desde o consumidor final (com planos individuais, familiares e pré/pós-pagos) até o mercado corporativo (com serviços de nuvem, segurança digital e dados via Claro Empresas).

### Produtos analisados

1. Gestão de conta e consumo de dados em tempo real pelo app Minha Claro.
2. Acesso a plataformas de entretenimento unificadas via Claro tv+.
3. Recargas, contratação de pacotes extras e suporte técnico digital.
4. Planos passaporte para uso de voz e dados no exterior.

### Funcionamento

1. A utilização dos serviços da Claro é centralizada principalmente por meios digitais e pelos equipamentos instalados na residência ou dispositivo móvel do cliente.
2. Ativação e Uso Móvel: Insira o SIM Card (chip) ou configure o eSIM no smartphone. A rede móvel é detectada automaticamente para chamadas e dados.
3. Serviços Residenciais (Wi-Fi e TV): O roteador e o decodificador/box da TV são instalados por um técnico. A conexão Wi-Fi é acessada via nome de rede e senha indicados na etiqueta do equipamento.
5. Gerenciamento pelo App (Minha Claro): Baixe o aplicativo Minha Claro Móvel ou Minha Claro Residencial (disponíveis para iOS e Android), faça login com CPF e senha para visualizar faturas, mudar de plano, consultar consumo de internet ou solicitar visitas técnicas.

### Pontos Fortes

1. Ampla Cobertura e Velocidade: Líder em cobertura e velocidade de internet móvel (4G/5G) em diversas regiões do Brasil, com infraestrutura de fibra de alta capacidade.
2. Combo e Unificação de Serviços: Facilidade de concentrar móvel, banda larga e TV em uma única fatura, garantindo descontos progressivos (Claro Multi).
3. Plataforma de Conteúdo (Claro tv+): Excelente integração entre canais de TV aberta/fechada e apps de streaming diretamente no mesmo dispositivo ou aplicativo.
4. Inovação Tecnológica: Pioneirismo na expansão da rede 5G e em soluções de e-SIM no país.

### Pontos Fracos

1. Atendimento ao Cliente: Relatos recorrentes de instabilidade na resolução de problemas complexos através dos canais de suporte telefônico e do robô virtual.
2. Faturamento e Cobranças: Reclamações frequentes sobre reajustes anuais acima da expectativa ou alterações de valores no fim do período de fidelidade.
3. Instabilidade de Sinal Localizada: Em determinadas áreas periféricas ou do interior, a oscilação do sinal de banda larga residencial e móvel ainda pode ser um problema.
4. Fidelização Rígida: A maioria dos contratos residenciais exige fidelidade de 12 meses, aplicando multas em caso de cancelamento antecipado.

---

## Empresa Analisada: Lyra M2M

### Visão geral

A Lyra M2M é a divisão de conectividade e gestão de SIM Cards M2M e IoT do Grupo Lyra Brasil, fundada originalmente como provedora global de infraestrutura e gateways de pagamentos e transações financeiras.

O público-alvo da Lyra M2M é predominantemente B2B (Business-to-Business), composto por integradores de tecnologia, desenvolvedores de hardware, prestadores de serviços e grandes corporações que necessitam de conectividade crítica e monitorada para seus dispositivos.

### Produtos Analisados

1. SIM Card Mono Operadora: Chip físico M2M associado a uma única operadora de telefonia móvel. Indicado para operações com alta demanda de tráfego de dados (como transmissão de vídeo) e em locais com cobertura geograficamente estável de uma determinada operadora.
2. SIM Card Multioperadora: Chip M2M inteligente capaz de alternar entre diferentes operadoras em um único SIM físico, garantindo redundância de sinal e expansão de cobertura em áreas rurais ou em deslocamento.
3. eSIM Lyra M2M (eUICC): Solução digitalizada de nova geração com provisionamento remoto (Over-The-Air - OTA). Permite armazenar e alternar remotamente o perfil de até 9 operadoras no mesmo chip sem necessidade de intervenção física ou substituição de hardware.
4. Plataforma de Gestão Lyra M2M: Portal SaaS em tempo real com dashboard para controle de pacotes de dados, monitoramento individual de chips, acionamento de travas de segurança (IMEI Lock), diagnóstico de rede e integração via APIs RESTful com sistemas de terceiros.

### Funcionamento

A Lyra M2M atua como provedora de conectividade gerenciada multi-operadora e gestão de SIM Cards M2M e eSIM. A empresa fornece dados para terminais de pagamento (POS), câmeras de segurança com reconhecimento facial, rastreamento de frotas e cidades inteligentes. Sua plataforma em nuvem oferece monitoramento de consumo em tempo real, gestão de APNs privadas e alertas de uso indevido.

### Pontos Fortes

1. Forte presença em meios de pagamento e segurança pública/privada.
2. Plataforma de gestão com dashboard em tempo real e monitoramento por aplicativo.
3. Recurso nativo de detecção de troca não autorizada de chip (IMEI Lock).
4. Herança do setor financeiro que garante criptografia rigorosa e conformidade nativa para a proteção de dados sensíveis.

### Pontos Fracos

1. Foco prioritário em redes celulares (2G/3G/4G/5G/eSIM), com menor integração nativa com redes LPWAN não-celulares (como LoRaWAN privado).
2. Customização de hardware e prototipagem do dispositivo de borda ficam a encargo do cliente final.
3. A solução depende da cobertura e do tempo de resposta das operadoras parceiras em falhas físicas de rede.
4. Modelo comercial B2B focado em escala, gerando custos de entrada pouco atraentes para pequenos protótipos ou startups em estágio inicial.

---

## Empresa analisada: ARQIA

### Visão geral

A Arqia é a unidade de negócios da Datora Telecom voltada exclusivamente para soluções de IoT e M2M. Atua no modelo MVNO (Operadora Virtual de Rede Móvel), utilizando a infraestrutura física de grandes operadoras de telecomunicações combinada a uma plataforma proprietária de gestão de conectividade. Seu público-alvo principal são integradores, empresas de rastreamento veicular, fintechs (máquinas de cartão/POS), utilities e indústrias que necessitam de conectividade gerenciada e suporte técnico especializado.

### Produtos analisados

- Arqia Core / Plataforma M2M: plataforma proprietária de gestão do ciclo de vida dos SIM Cards em tempo real (ativação, bloqueio, consumo e diagnósticos).
- Chips M2M Multi-operadora / Roaming Nacional: SIM Cards (físicos e eSIM) com redundância automática de sinal entre as principais operadoras de telecom do país.
- Conectividade para Meios de Pagamento (POS/POS IP): pacotes e chips otimizados especificamente para maquininhas de cartão com baixa latência e alta disponibilidade.
- APIs de Integração M2M: conjunto de conectores para que o cliente integre a gestão dos SIM Cards diretamente ao seu próprio sistema ou ERP.

### Funcionamento

Conectividade multi-rede: o dispositivo do cliente (rastreador, POS, medidor ou gateway) utiliza o SIM Card da Arqia para se conectar à antena com melhor sinal disponível no local (tecnologias 2G, 3G, 4G, NB-IoT ou LTE-M), operando em regime de roaming ou troca de perfil.

Ingestão e roteamento: o tráfego de dados gerado pelo dispositivo passa pelos servidores da Arqia (Core de Rede próprio sobre a infraestrutura parceira), garantindo segurança, controle de dados e túneis VPN privados.

Gestão centralizada e integração via API: o cliente acessa a plataforma Arqia Core para monitorar em tempo real o consumo de megabytes, status de conexão, diagnóstico de falhas e automação de regras de faturamento, integrando esses controles ao seu ERP via APIs.

Aplicação focada em conectividade pura (diferencial de modelo): ao contrário de operadoras tradicionais que vendem a aplicação final pronta, a Arqia foca em entregar conectividade resiliente e ferramentas para que integradores construam suas próprias soluções.

### Pontos Fortes

- Redundância e multi-operadora: por ser uma MVNO, consegue entregar maior disponibilidade em campo ao chavear entre redes (Claro, Vivo, TIM), reduzindo pontos cegos geográficos.
- Foco e especialização em B2B/M2M: diferente de grandes operadoras cujo foco principal ainda é o cliente final residencial/móvel, a estrutura da Arqia é totalmente dedicada a projetos M2M e IoT.
- Plataforma de gestão flexível e intuitiva: interface voltada para o gestor técnico/operacional, permitindo diagnósticos avançados de conectividade e controle granular por chip.
- Atendimento consultivo e próximo: suporte técnico mais ágil e especializado em demandas de engenharia de IoT do que os canais corporativos engessados das grandes operadoras.

### Pontos Fracos

- Sem infraestrutura de acesso própria: como depende das antenas e torres das operadoras tradicionais, fica vulnerável a instabilidades gerais na camada física de radiofrequência dessas parceiras.
- Ausência de soluções de aplicação "end-to-end": não oferece aplicações prontas para o cliente final (como dashboards de telemetria de iluminação ou sensores específicos), exigindo que o cliente desenvolva o software ou contrate um integrador.
- Escala de infraestrutura menor que operadoras Tier 1: embora robusta para o mercado B2B, não possui a mesma força de investimento em infraestrutura pura de rede que uma operadora de cobertura nacional direta.
- Dependência de terceiros para expansão de tecnologias como NB-IoT: o cronograma de liberação e expansão de novas tecnologias de rede celular depende do ritmo de implantação das donas das redes físicas.

---

# Requisitos não triviais

1. Funcionalidade que permite que o usuário adicione regras de funcionamento do sistema sem precisar alterar o código diretamente pela interface. Por exemplo, se o produto for um portão eletrônico, seria possível configurar o comando: "Se o portão for aberto fora do horário estabelecido pelo próprio usuário, enviar um alerta", sem necessidade de mexer no back-end. Além disso, uma mesma regra pode acionar mais de uma ação ao mesmo tempo, como, seguindo o mesmo exemplo, enviar o alerta e travar o portão automaticamente.

2. Exibir, em uma escala ou porcentagem, a "saúde" do aparelho, considerando não apenas o nível de bateria, mas também a qualidade da recepção de sinal, o tempo de resposta e outros fatores. Essa nota é calculada com base no histórico de funcionamento do aparelho ao longo do tempo, o que permite identificar uma possível falha antes que ela aconteça.

3. Catálogo de configurações prontas para um mesmo tipo de aparelho. Um mesmo equipamento pode ser utilizado de diferentes formas dependendo do ambiente, por exemplo, uma geladeira pode estar em uma cozinha convencional, em um restaurante ou em um açougue. Ao selecionar o local de uso, o sistema aplica automaticamente a configuração mais adequada para que o aparelho funcione da melhor forma naquele contexto.
   
4. Registrar as alterações realizadas no sistema, permitindo identificar quem fez a alteração e em que horário ela ocorreu. Esse controle vale tanto para ações de administradores quanto de usuários comuns, tornando a resolução de problemas e o acompanhamento do uso muito mais fáceis, além de reforçar a segurança do sistema.
