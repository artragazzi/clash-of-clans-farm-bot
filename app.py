import pyautogui
import time
import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


#se Enloquecer, jogue o mouse para o canto superior esquerdo
pyautogui.FAILSAFE = True

#IMAGENS
#Iniciar Ataque
BOTAO_ATACAR = os.path.join("images", "botao_atacar.png")
BOTAO_PROCURAR_PARTIDA = os.path.join("images","botao_procurar_partida.png")
BOTAO_INICIAR_ATAQUE = os.path.join("images","botao_iniciar_ataque.png")

#Achou Vila
INDICADOR_ACHOU_VILA_IMAGEM = os.path.join("images","indicar_achou_vila.png")
PROXIMA_VILA = os.path.join("images","proxima_vila.png")
LOCAL_DROP_TROPA = os.path.join("images","local_drop_tropas.png")

#OBSTACULOS
LOCAL_OBS1 = os.path.join("images","obs_1.png")
LOCAL_OBS2 = os.path.join("images","obs_2.png")
LOCAL_OBS3 = os.path.join("images","obs_3.png")
LOCAL_OBS4 = os.path.join("images","obs_4.png")
LOCAL_OBS5 = os.path.join("images","obs_5.png")

#Ataque
SELECAO_GUARDIAO = os.path.join("images","guardiao.png")
SELECAO_TROPA = os.path.join("images","tropa.png")
FINALIZAR_ATAQUE = os.path.join("images","finalizar_ataque.png")
SELECAO_SERVO = os.path.join("images","servo.png")
SELECAO_CAMPEA = os.path.join("images","campea.png")

#Muros
MURO_ESCOLHIDO = os.path.join("images","muro.png")
MURO_ESCOLHIDO_MELHORAR_OURO = os.path.join("images","muro_melhorar_ouro.png")
MURO_ESCOLHIDO_MELHORAR_ELIXIR = os.path.join("images","muro_melhorar_elixir.png")

CONFIRMAR_MURO_ESCOLHIDO = os.path.join("images","confirmar_muro.png")





def clicar_para_atacar():
    print("Iniciando bot...")
    time.sleep(2)
    #Botao Atacar
    while True:
        try:
            coordernada_botao_atacar = pyautogui.locateCenterOnScreen(BOTAO_ATACAR, confidence=0.8)
            if coordernada_botao_atacar is not None:
                print(f"Imagens botões iniciar ataque encontrados: {coordernada_botao_atacar}")
                #Mover para botao de atacar
                pyautogui.moveTo(coordernada_botao_atacar, duration=0.2)
                pyautogui.click()
                time.sleep(1)
                break # Sai do loop e vai para o próximo passo
                
            else:
                print("Não consegue achar a imagem do botão de ataque. Tentando novamente...")
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Erro: Arquivo de imagem Atacar não foi localizado ou formato incompatível. Tentando novamente...")
            time.sleep(1)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            time.sleep(1)
        
    #Buscar partida
    while True:
        try:
            coordernada_botao_procurar_partida = pyautogui.locateCenterOnScreen(BOTAO_PROCURAR_PARTIDA, confidence=0.8)
            if coordernada_botao_procurar_partida is not None:
                print(f"Imagens botões buscar partida encontrados: {coordernada_botao_procurar_partida}")
                pyautogui.moveTo(coordernada_botao_procurar_partida, duration=0.2)
                pyautogui.click()
                time.sleep(1)
                break # Sai do loop e vai para o próximo passo
                
            else:
                print("Não consegue achar a imagem do botão de procurar partida. Tentando novamente...")
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Erro: Arquivo de imagem Procurar partida não foi localizado ou formato incompatível. Tentando novamente...")
            time.sleep(1)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            time.sleep(1)
        
    
    #Iniciar ataque
    while True:
        try:
            coordernada_botao_iniciar_ataque = pyautogui.locateCenterOnScreen(BOTAO_INICIAR_ATAQUE, confidence=0.8)
            if coordernada_botao_iniciar_ataque is not None:
                print(f"Imagens botões buscar partida encontrados: {coordernada_botao_iniciar_ataque}")
                pyautogui.moveTo(coordernada_botao_iniciar_ataque, duration=0.2)
                pyautogui.click()
                time.sleep(1)
                break # Sai do loop e finaliza a função
                
            else:
                print("Não consegue achar a imagem do botão de iniciar ataque. Tentando novamente...")
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Erro: Arquivo de imagem iniciar ataque não foi localizado ou formato incompatível. Tentando novamente...")
            time.sleep(1)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            time.sleep(1)
        
def verifica_achou_vila():

    print("\nIniciando verificação...")
    time.sleep(3)
    
    # Inicializa as variáveis
    coord_indicador = None
    coord_proxima = None

    # 1. Tenta achar o Indicador da Vila
    try:
        coord_indicador = pyautogui.locateCenterOnScreen(INDICADOR_ACHOU_VILA_IMAGEM, confidence=0.7)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: INDICADOR_ACHOU_VILA_IMAGEM")

    # 2. Tenta achar o Botão de Próxima Vila
    try:
        coord_proxima = pyautogui.locateCenterOnScreen(PROXIMA_VILA, confidence=0.8)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: PROXIMA_VILA")
        
    
    # Se achou a vila
    if coord_indicador is not None:
        print(f"[+] Tudo certo para atacar! Vila identificada.")
        time.sleep(2)
        return True # Retorna True para sinalizar que o loop no __main__ pode parar
                
    else:
        print("[!] Condições para ataque não atendidas. Pulando vila...")
        if coord_proxima is not None:
            pyautogui.moveTo(coord_proxima, duration=0.2)
            pyautogui.click()
            print("[+] Clicou em Próxima Vila.")
            time.sleep(5) # Tempo essencial para aguardar o jogo carregar a próxima tela
        else:
            print("[-] Erro crítico: O botão 'Próxima Vila' não foi encontrado.")
            time.sleep(2)
        return False # Retorna False para continuar procurando no loop do __main__


def dropar_tropas():
    print("Iniciando drop tropas...")
    time.sleep(2)
    
    # Inicializa as variáveis
    coord_dg_eletrico = None
    coord_guardiao = None
    
    #Seleção e drop Dg Eletrico e lança
    
    # 1. Tenta achar o Dragao Eletrico
    try:
        coord_dg_eletrico = pyautogui.locateCenterOnScreen(SELECAO_TROPA, confidence=0.8)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: SELECAO_TROPA")
    
    if coord_dg_eletrico is not None:
        pyautogui.moveTo(coord_dg_eletrico, duration=0.2)
        pyautogui.click()
        print("[+] Clicou no Dragao Eletrico.")
        
        time.sleep(0.2)
        
        pyautogui.moveTo(260,480, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(3)
        pyautogui.mouseUp()
        
        
    #Seleção e drop guardiao e lança
    
    # 2. Tenta achar a tropa
    try:
        coord_guardiao = pyautogui.locateCenterOnScreen(SELECAO_GUARDIAO, confidence=0.8)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: SELECAO_GUARDIAO")
    
    if coord_guardiao is not None:
        pyautogui.moveTo(coord_guardiao, duration=0.2)
        pyautogui.click()
        print("[+] Clicou no Guardiao.")
        
        time.sleep(0.2)
        
        pyautogui.moveTo(260,480, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
        
         # 3. Tenta achar o Servo
    try:
        coord_servo = pyautogui.locateCenterOnScreen(SELECAO_SERVO, confidence=0.8)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: SELECAO_SERVO")
    
    if coord_servo is not None:
        pyautogui.moveTo(coord_servo, duration=0.2)
        pyautogui.click()
        print("[+] Clicou no Servo.")
        
        time.sleep(0.2)
        
        pyautogui.moveTo(260,480, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
    
    
         # 4. Tenta achar o Campea
    try:
        coord_campea = pyautogui.locateCenterOnScreen(SELECAO_CAMPEA, confidence=0.8)
    except (pyautogui.ImageNotFoundException, Exception):
        print(f"[-] Imagem não encontrada: SELECAO_SERVO")
    
    if coord_campea is not None:
        pyautogui.moveTo(coord_campea, duration=0.2)
        pyautogui.click()
        print("[+] Clicou no Servo.")
        
        time.sleep(0.2)
        
        pyautogui.moveTo(260,480, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
        
        
        

def monitorar_ataque():
    ja_acabou_ataque = False
    
    # Mudamos para 'while not': roda enquanto o ataque NÃO acabou
    while not ja_acabou_ataque:
        print("[i] Monitorando fim do ataque...")
        time.sleep(2) # Timeout pra nao checar toda hora
        
        try:
            coord_finalizar = pyautogui.locateCenterOnScreen(FINALIZAR_ATAQUE, confidence=0.8)
            if coord_finalizar is not None:
                pyautogui.moveTo(coord_finalizar, duration=0.2)
                pyautogui.click()
                print("[+] Botão de finalizar encontrado! Ataque encerrado.")
                time.sleep(1)
                return True # Sai da função com sucesso
        except (pyautogui.ImageNotFoundException, Exception):
            # Ocultamos ou simplificamos o print para não poluir o terminal a cada 2 segundos
            pass   
    
    

def enviar_captura():
    print("\n[TELEGRAM] Tirando screenshot e enviando...")
    
    # Puxa as credenciais das variáveis globais (que foram carregadas do .env)
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    # Define um nome temporário para o arquivo de imagem
    nome_arquivo = "screenshot_temp.png"
    
    try:
        time.sleep(2)
        # 1. Tira a captura de tela e salva no computador
        screenshot = pyautogui.screenshot()
        screenshot.save(nome_arquivo)
        
        # 2. Configura a URL da API do Telegram para envio de fotos (sendPhoto)
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        
        # 3. Abre o arquivo salvo e envia via POST para o Telegram
        with open(nome_arquivo, "rb") as foto:
            payload = {"chat_id": chat_id, "caption": "Recurso Atual"}
            files = {"photo": foto}
            
            resposta = requests.post(url, data=payload, files=files)
            
            # Verifica se o Telegram recebeu com sucesso (Status 200)
            if resposta.status_code == 200:
                print("[TELEGRAM] Screenshot enviada com sucesso!")
            else:
                print(f"[-] Erro ao enviar para o Telegram. Status: {resposta.status_code} - {resposta.text}")
                
    except Exception as e:
        print(f"[-] Falha na função de enviar captura: {e}")
        
    finally:
        # 4. Remove o arquivo de imagem do PC para não acumular lixo na pasta do projeto
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            
            
def verificar_comandos_telegram():
    token = os.getenv("TELEGRAM_TOKEN")
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    
    try:
        # Pega as últimas mensagens enviadas para o bot
        resposta = requests.get(url).json()
        
        if resposta.get("ok") and resposta.get("result"):
            # Pega a última mensagem recebida
            ultima_mensagem = resposta["result"][-1]["message"]["text"].strip()
            
            # Se for /stop, entra no loop de pausa
            if ultima_mensagem == "/stop":
                print("\n[TELEGRAM] Bot PAUSADO via comando /stop. Aguardando /continue...")
                
                # Fica preso aqui até você mandar /continue
                while True:
                    time.sleep(3)
                    resp_pausa = requests.get(url).json()
                    if resp_pausa.get("ok") and resp_pausa.get("result"):
                        msg_pausa = resp_pausa["result"][-1]["message"]["text"].strip()
                        if msg_pausa == "/continue":
                            print("[TELEGRAM] Bot RETOMADO via comando /continue!")
                            break
    except Exception as e:
        # Se der erro de internet ou API, ignora para não travar o bot
        pass


def upar_muro():
    print("Upando muro...")
    time.sleep(2)
    
    # Selecionando o Muro
    try:
        coord_muro = pyautogui.locateCenterOnScreen(MURO_ESCOLHIDO, confidence=0.9)
        if coord_muro is not None:
            print(f"Muro encontrado: {coord_muro}")
            # Mover para muro
            pyautogui.moveTo(coord_muro, duration=0.2)
            pyautogui.click()
            time.sleep(0.2)
                            
        else:
            print("Não consegui achar a imagem do muro... Seguindo o fluxo.")
            return # Sai da função imediatamente e segue o jogo
    except pyautogui.ImageNotFoundException:
        print("Erro: Arquivo de imagem Muro não foi localizado ou formato incompatível. Seguindo o fluxo...")
        return # Sai da função imediatamente e segue o jogo
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return # Sai da função imediatamente e segue o jogo
    
    # Escolhendo qual forma de upar
    coord_mineiro_escolhido = None

    # 1. Tenta achar o botão de ouro
    try:
        coord_melhorar_ouro = pyautogui.locateCenterOnScreen(MURO_ESCOLHIDO_MELHORAR_OURO, confidence=0.91)
    except (pyautogui.ImageNotFoundException, Exception):
        coord_melhorar_ouro = None

    # 2. Tenta achar o botão de elixir
    try:
        coord_melhorar_elixir = pyautogui.locateCenterOnScreen(MURO_ESCOLHIDO_MELHORAR_ELIXIR, confidence=0.91)
    except (pyautogui.ImageNotFoundException, Exception):
        coord_melhorar_elixir = None


    # --- Decisão de qual recurso usar ---
    if coord_melhorar_ouro is not None:
        coord_mineiro_escolhido = coord_melhorar_ouro
        print(f"[+] Botão de OURO encontrado! Usando coordenada: {coord_mineiro_escolhido}")
        
    elif coord_melhorar_elixir is not None:
        coord_mineiro_escolhido = coord_melhorar_elixir
        print(f"[+] Botão de ELIXIR encontrado! Usando coordenada: {coord_mineiro_escolhido}")
        
    else:
        print("[-] Não encontrei nenhum dos dois botões de melhoria (Ouro ou Elixir). Seguindo o fluxo.")
        # Se abriu o muro mas não achou os botões, não há o que clicar. Apenas sai da função.
        return 


    # --- Executa o clique final se algum foi escolhido ---
    if coord_mineiro_escolhido is not None:
        pyautogui.moveTo(coord_mineiro_escolhido, duration=0.2)
        pyautogui.click()
        print("[+] Muro indo para confirmação!")
        time.sleep(0.2)
        
    
    # Selecionando confirmação
    try:
        coord_confirmar_muro = pyautogui.locateCenterOnScreen(CONFIRMAR_MURO_ESCOLHIDO, confidence=0.70)
        # CORREÇÃO: Validando a variável correta da confirmação
        if coord_confirmar_muro is not None:
            print(f"Confirmação achada: {coord_confirmar_muro}")
            # Mover para botao de confirmação
            pyautogui.moveTo(coord_confirmar_muro, duration=0.2)
            pyautogui.click()
            time.sleep(0.2)
                            
        else:
            print("Não consegui achar a imagem de confirmação do muro... Seguindo o fluxo.")
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("Erro: Arquivo de imagem de confirmação Muro não foi localizado ou formato incompatível. Seguindo o fluxo...")
        time.sleep(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        time.sleep(1)
      
        
if __name__ == "__main__":
    
    contador_envio_imagem = 0
    
    while True:
        # Checa se você mandou /stop antes de iniciar as ações da rodada
        verificar_comandos_telegram()
        
        clicar_para_atacar()
        
        # Loop que força o bot a rodar a verificação até achar uma vila válida
        sucesso_busca = False
        while not sucesso_busca:
            sucesso_busca = verifica_achou_vila()
            
        dropar_tropas()
        monitorar_ataque()
        
        # Soma 1 ao contador toda vez que um ataque termina
        contador_envio_imagem += 1
        time.sleep(3)
        upar_muro() # Executa a tentativa de upgrade de muro com retornos seguros
        
        # Envia imagem a cada 1 ataque (conforme seu código atual)
        if contador_envio_imagem >= 2:
            time.sleep(1)
            enviar_captura()
            contador_envio_imagem = 0
            
        time.sleep(2)