import re
import pandas as pd

# A variável dados contendo o texto
dados = '''Resultado da Consulta: 14 Processo(s) encontrado(s)
Nova Pesquisa
Imprimir

As informações aqui contidas não produzem efeitos legais. Somente a publicação no DJERJ oficializa despachos e decisões e estabelece prazos.

TJRJ - 1ª Instância - 20/05/2025 04:04

Origem: 1ª Instância
Comarca: Todas as Comarcas
Competência: Cível
Nome Pesquisado: Fundação Getulio Vargas
Período: 2024 a 2025

Tipo de Ordenação *
Classificação
Processo: 0092838-17.2024.8.19.0001
Requerente: ARTUR NATAN DOS SANTOS
Requerido: FUNDACAO GETULIO VARGAS
Descrição Arquivamento

Comarca: Comarca de Barra Mansa

Serventia: Cartório da 4ª Vara Cível
...'''  # Continue com os dados fornecidos

# Expressão regular para extrair os dados
pattern = r'Processo:\s*(?P<processo>\S+)\nRequerente:\s*(?P<requerente>.*?)\nRequerido:\s*(?P<requerido>.*?)\nDescrição\s*(?P<descricao>.*?)\n\nComarca:\s*(?P<comarca>.*?)\n\nServentia:\s*(?P<serventia>.*?)\n'

# Encontrar todos os matches
matches = re.finditer(pattern, dados, re.DOTALL)

# Criar uma lista para armazenar os dados extraídos
dados_extraidos = []

# Iterar sobre os matches e extrair os dados
for match in matches:
    dado = {
        "Número do Processo": match.group('processo'),
        "Requerente": match.group('requerente'),
        "Requerido": match.group('requerido'),
        "Descrição": match.group('descricao'),
        "Comarca": match.group('comarca'),
        "Serventia": match.group('serventia'),
    }
    dados_extraidos.append(dado)

# Criar um DataFrame do pandas a partir da lista
df = pd.DataFrame(dados_extraidos)

# Salvar o DataFrame em um arquivo Excel
df.to_excel("dados_processos.xlsx", index=False)

print("Os dados foram salvos em 'dados_processos.xlsx'.")