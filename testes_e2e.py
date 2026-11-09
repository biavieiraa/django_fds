import os
import random
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BzuTechE2ETests(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        
        # Ativa o modo invisível apenas no GitHub Actions (CI)
        if os.environ.get('HEADLESS') == 'true' or os.environ.get('CI'):
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=options
        )
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Pausa final antes de fechar a janela em cada teste
        time.sleep(2)
        self.driver.quit()

    def test_01_quiz_cenario_empresa(self):
        """História 1: Quiz para descobrir o cenário da empresa do usuário (no Chat IA)"""
        driver = self.driver
        
        # 1. Começa na página inicial do app (forum)
        driver.get(f"{self.live_server_url}/forum/")
        time.sleep(1.5)

        # 2. Navega para a página da IA/Chat onde fica o quiz
        driver.get(f"{self.live_server_url}/forum/ia/")
        time.sleep(1.5)

        # 3. Fecha o popup inicial se ele aparecer na tela
        popup_skip = driver.find_elements(By.ID, "bzu-popup-skip")
        if popup_skip and popup_skip[0].is_displayed():
            popup_skip[0].click()
            time.sleep(1)

        # 4. Inicia o quiz clicando no botão da sidebar (caso não tenha iniciado sozinho)
        opcoes = driver.find_elements(By.CLASS_NAME, "quiz-chat-opcao")
        if not opcoes:
            btn_quiz = driver.find_element(By.ID, "btn-quiz")
            btn_quiz.click()
            time.sleep(1.5)
            opcoes = driver.find_elements(By.CLASS_NAME, "quiz-chat-opcao")

        # 5. Clica no botão "Vamos lá" para iniciar as perguntas
        if opcoes:
            opcoes[0].click()
            time.sleep(1.5)

        # 6. Responde consecutivamente às 6 perguntas escolhendo opções aleatórias
        for _ in range(6):
            opcoes = driver.find_elements(By.CLASS_NAME, "quiz-chat-opcao")
            if opcoes:
                opcao_sorteada = random.choice(opcoes)
                opcao_sorteada.click()  # Clica em uma resposta aleatória
                time.sleep(1.2)        # Pausa para visualização na gravação
            else:
                break

        # 7. Validação do perfil gerado ao final do quiz
        time.sleep(2)
        self.assertIn("Seu perfil", driver.page_source)

    def test_02_historico_conversas_chatbot(self):
        """História 2: Histórico de conversas com o Chatbot BrIAn"""
        driver = self.driver

        # 1. Começa na página inicial
        driver.get(f"{self.live_server_url}/forum/")
        time.sleep(1.5)

        # 2. Navega para a página da IA
        driver.get(f"{self.live_server_url}/forum/ia/")
        time.sleep(1.5)

        # 3. Clica direto no botão "Fazer login" dentro do popup modal
        popup_login = driver.find_elements(By.CSS_SELECTOR, "#bzu-popup .bzu-popup-btn-primary")
        if popup_login and popup_login[0].is_displayed():
            popup_login[0].click()
        else:
            links_login = driver.find_elements(By.XPATH, "//a[contains(@href, 'login')]")
            if links_login:
                links_login[0].click()
            else:
                driver.get(f"{self.live_server_url}/forum/login/")
        time.sleep(1.5)

        # 4. Clica para criar conta (registro)
        links_register = driver.find_elements(By.XPATH, "//a[contains(@href, 'register')]")
        if links_register:
            links_register[0].click()
        else:
            driver.get(f"{self.live_server_url}/forum/register/")
        time.sleep(1.5)

        # 5. Preenche cadastro com usuário e senha de teste
        inputs_text = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        inputs_pass = driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
        
        if inputs_text:
            inputs_text[0].send_keys("teste_execucao")
        for inp in inputs_pass:
            inp.send_keys("Bryan_eh_incrivel")
            
        time.sleep(1)
        btn_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn_submit.click()
        time.sleep(2)

        # 6. Volta para a página da IA
        driver.get(f"{self.live_server_url}/forum/ia/")
        time.sleep(1.5)

        # 7. Clica no botão "Agora não" do quiz interativo se ele for exibido no chat
        btn_agora_nao = driver.find_elements(By.XPATH, "//button[contains(text(), 'Agora não')]")
        if btn_agora_nao and btn_agora_nao[0].is_displayed():
            btn_agora_nao[0].click()
            time.sleep(1.5)

        # 8. Clica para abrir uma nova conversa antes do primeiro envio
        btn_nova = driver.find_element(By.CSS_SELECTOR, ".btn-new-chat")
        btn_nova.click()
        time.sleep(1.5)

        # 9. Clica no campo de texto e envia a pergunta "o que é IoT"
        input_chat = driver.find_element(By.ID, "user-input")
        input_chat.click()
        time.sleep(0.5)
        input_chat.send_keys("o que é IoT?")
        time.sleep(1)
        btn_send = driver.find_element(By.CSS_SELECTOR, ".btn-send-icon")
        btn_send.click()
        time.sleep(3)

        # 10. Clica para abrir outra conversa com a IA
        btn_nova = driver.find_element(By.CSS_SELECTOR, ".btn-new-chat")
        btn_nova.click()
        time.sleep(2)

        # 11. Clica no campo de texto e envia a pergunta "o que é a Bzu Tech"
        input_chat = driver.find_element(By.ID, "user-input")
        input_chat.click()
        time.sleep(0.5)
        input_chat.send_keys("o que é a Bzu Tech?")
        time.sleep(1)
        btn_send = driver.find_element(By.CSS_SELECTOR, ".btn-send-icon")
        btn_send.click()
        time.sleep(3)

        # 12. Clica em "+ Nova conversa"
        btn_nova = driver.find_element(By.CSS_SELECTOR, ".btn-new-chat")
        btn_nova.click()
        time.sleep(2)

        # 13. Volta para a primeira conversa ("o que é IoT")
        links_conversas = driver.find_elements(By.CLASS_NAME, "conversation-link")
        link_iot = [l for l in links_conversas if "IoT" in l.text or "IoT" in (l.get_attribute("title") or "")]
        if link_iot:
            link_iot[0].click()
        elif links_conversas:
            links_conversas[-1].click()
        time.sleep(2.5)

        # 14. Volta para a segunda conversa ("o que é a Bzu Tech")
        links_conversas = driver.find_elements(By.CLASS_NAME, "conversation-link")
        link_bzu = [l for l in links_conversas if "Bzu" in l.text or "Bzu" in (l.get_attribute("title") or "")]
        if link_bzu:
            link_bzu[0].click()
        elif len(links_conversas) >= 2:
            links_conversas[0].click()
        time.sleep(2.5)

        # 15. Deixa mostrando o histórico de conversas na lateral
        sidebar = driver.find_element(By.CLASS_NAME, "chat-sidebar")
        self.assertTrue(sidebar.is_displayed())
        time.sleep(3)

    def test_03_exibicao_empresas_parceiras(self):
        """História 3: Exibição das empresas parceiras da Bzu Tech"""
        driver = self.driver

        # 1. Começa na página inicial do app (forum)
        driver.get(f"{self.live_server_url}/forum/")
        time.sleep(1.5)

        # 2. Navega para a página Sobre a Empresa (Parceiros)
        driver.get(f"{self.live_server_url}/forum/sobre-empresa/")
        time.sleep(1.5)

        # 3. Rola a tela até a seção do Carrossel de Parceiros ("Casos reais")
        carrossel = driver.find_element(By.ID, "carrossel-casos")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", carrossel)
        time.sleep(2)

        # 4. Clica na seta da direita (Próximo) 3 vezes até chegar na Parlacom
        btn_proximo = driver.find_element(By.CSS_SELECTOR, ".carrossel__seta[data-direcao='1']")
        
        for _ in range(3):
            btn_proximo.click()
            time.sleep(1.5)

        # 5. Validação da exibição do carrossel e conteúdo
        self.assertTrue(carrossel.is_displayed())
        self.assertIn("Parlacom", driver.page_source)
        self.assertIn("M. Dias Branco", driver.page_source)