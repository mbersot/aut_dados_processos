import re, os
import pandas as pd
import send_email
from config import login_url
from mensagem import exibir_mensagem

dados_extraidos = []
def processa_autor(dados):
    # A variável dados contendo o texto
    
    # Expressão regular para extrair os dados
    pattern = r'Processo:\s*(?P<processo>\S+)\nAutor:\s*(?P<autor>.*?)\nRéu:\s*(?P<reu>.*?)\nDescrição\s*(?P<descricao>.*?)\n\nComarca:\s*(?P<comarca>.*?)\n\nServentia:\s*(?P<serventia>.*?)\n'

    # Encontrar todos os matches
    matches = re.finditer(pattern, dados, re.DOTALL)

    # Iterar sobre os matches e extrair os dados
    for match in matches:
        dado = {
        "Número do Processo": match.group('processo'),
        "Requerente/Impetrante/Embargante/Autor": match.group('autor'),
        "Requerido/Impetrado/Embargado/Réu": match.group('reu'),
        "Descrição": match.group('descricao'),
        "Comarca": match.group('comarca'),
        "Serventia": match.group('serventia'),
        }
        dados_extraidos.append(dado)
        
def processa_embargante(dados):
    # A variável dados contendo o texto
    
    # Expressão regular para extrair os dados
    pattern = r'Processo:\s*(?P<processo>\S+)\nEmbargante:\s*(?P<embargante>.*?)\nEmbargado:\s*(?P<embargado>.*?)\nDescrição\s*(?P<descricao>.*?)\n\nComarca:\s*(?P<comarca>.*?)\n\nServentia:\s*(?P<serventia>.*?)\n'

    # Encontrar todos os matches
    matches = re.finditer(pattern, dados, re.DOTALL)

    # Iterar sobre os matches e extrair os dados
    for match in matches:
        dado = {
            "Número do Processo": match.group('processo'),
            "Requerente/Impetrante/Embargante/Autor": match.group('embargante'),
            "Requerido/Impetrado/Embargado/Réu": match.group('embargado'),
            "Descrição": match.group('descricao'),
            "Comarca": match.group('comarca'),
            "Serventia": match.group('serventia'),
        }
        dados_extraidos.append(dado)


def processa_impetrante(dados):
    # A variável dados contendo o texto
    
    # Expressão regular para extrair os dados
    pattern = r'Processo:\s*(?P<processo>\S+)\nImpetrante:\s*(?P<impetrante>.*?)\nImpetrado:\s*(?P<impetrado>.*?)\nDescrição\s*(?P<descricao>.*?)\n\nComarca:\s*(?P<comarca>.*?)\n\nServentia:\s*(?P<serventia>.*?)\n'

    # Encontrar todos os matches
    matches = re.finditer(pattern, dados, re.DOTALL)

    # Iterar sobre os matches e extrair os dados
    for match in matches:
        dado = {
            "Número do Processo": match.group('processo'),
            "Requerente/Impetrante/Embargante/Autor": match.group('impetrante'),
            "Requerido/Impetrado/Embargado/Réu": match.group('impetrado'),
            "Descrição": match.group('descricao'),
            "Comarca": match.group('comarca'),
            "Serventia": match.group('serventia'),
        }
        dados_extraidos.append(dado)
        

def processa_dados(dados):
    # A variável dados contendo o texto
    
    # Expressão regular para extrair os dados
    pattern = r'Processo:\s*(?P<processo>\S+)\nRequerente:\s*(?P<requerente>.*?)\nRequerido:\s*(?P<requerido>.*?)\nDescrição\s*(?P<descricao>.*?)\n\nComarca:\s*(?P<comarca>.*?)\n\nServentia:\s*(?P<serventia>.*?)\n'

    # Encontrar todos os matches
    matches = re.finditer(pattern, dados, re.DOTALL)

    # Iterar sobre os matches e extrair os dados
    for match in matches:
        dado = {
            "Número do Processo": match.group('processo'),
            "Requerente/Impetrante/Embargante/Autor": match.group('requerente'),
            "Requerido/Impetrado/Embargado/Réu": match.group('requerido'),
            "Descrição": match.group('descricao'),
            "Comarca": match.group('comarca'),
            "Serventia": match.group('serventia'),
        }
        dados_extraidos.append(dado)
        
    processa_autor(dados)
    processa_embargante(dados)
    processa_impetrante(dados)
    exibir_mensagem("Armazenando dados em planilha!")
    df = pd.DataFrame(dados_extraidos)
    
    # Obtém o diretório raiz do arquivo atual
    pasta_raiz = os.path.dirname(os.path.abspath(__file__))
    # Adiciona a pasta 'temp' ao caminho
    pasta_temp = os.path.join('temp', 'dados_processados.xlsx')
    
    df.to_excel(pasta_temp, index=False)
    dadosAcesso = login_url()
    exibir_mensagem("Enviando planilha por e-mail!")
    send_email.enviar_email(dadosAcesso[0], dadosAcesso[1], dadosAcesso[3], dadosAcesso[3], dadosAcesso[5], pasta_temp)
    exibir_mensagem("Fim da automação!")