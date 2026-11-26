import yaml
import logging
import datetime
import os
import time

nomeLog = datetime.date.today()
nomeLog = str(nomeLog)
nomeLog = "./log/log-"+nomeLog+".log"
logging.basicConfig(level=logging.DEBUG, filename=nomeLog)

horaErro = datetime.datetime.now()
horaErro = str(horaErro)

arqConfig = diretorio_atual = os.getcwd()+r"\config.yaml"

#print(arqConfig)

try:
    def login_url ():
        with open(arqConfig, "r") as f:
            config = yaml.safe_load(f)

        usuario = config['credencialTimeSheet']['user']
        senha = config['credencialTimeSheet']['senha']
        projeto_alocado = config['credencialTimeSheet']['projeto_alocado']
        url = config['urls']['urlTimesheet']
        urlTimesheetColaborador = config['urls']['urlTimesheetColaborador']
        teste = config["commons"]["teste"]
        return usuario, senha, projeto_alocado, url, urlTimesheetColaborador, teste
    
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

else:
    
    logging.info(horaErro + " Inicio do erro")

finally:
    logging.info(horaErro + " Fim do erro")
    #print (login_url ())