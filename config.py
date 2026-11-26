import yaml
import logging
import datetime
import os
import time

pasta_raiz = os.path.dirname(os.path.abspath(__file__))
pasta_log = pasta_raiz + r"\log"
nomeLog = datetime.date.today()
nomeLog = f"log-{nomeLog}.log"
caminho_log = os.path.join(pasta_log, nomeLog)

if not os.path.exists(pasta_raiz + r"\log"):    
    os.makedirs(pasta_raiz + r"\log")
# Configuração do logging
logging.basicConfig(level=logging.DEBUG, filename=caminho_log)

horaErro = datetime.datetime.now()
horaErro = str(horaErro)

pasta_raiz= pasta_raiz
#pasta_raiz = pasta_raiz[:-10]
arqConfig = pasta_raiz+r"\config.yaml"

print("Arquivo de configuração carregado!")

try:
    def login_url ():
        with open(arqConfig, "r") as f:
            config = yaml.safe_load(f)

        usuario = config['usuario']
        senha = config['senha']
        url = config['url']
        destinatario = config['destinatario']
        assunto = config['assunto']
        corpo = config['corpo']
        caminho_chrome = config['caminho_chrome']
        teste = config['teste']
        return usuario, senha, url, destinatario, assunto, corpo, caminho_chrome, teste
    
    def type_slowly(element, text, delay=0.05):
        # Limpa o campo de entrada antes de digitar devagar
        #element.clear()
        time.sleep(0.1)  # Aguarda meio segundo após limpar o campo
        
        # Digita devagar no campo de entrada
        for char in text:
            element.type(char)
            time.sleep(delay)
        
except TypeError as e:
    e = str(e)
    e = horaErro + " - " + e
    logging.info(e)