from bs4 import BeautifulSoup as sp
import requests

# WEB crawler - FATEC São Caetano do Sul
# Melhorias:
#  - Criar uma lista com vários sites de clima e rodar um for com a qtde de sites passando cada item para requests.get

# Pega o conteudo da pagina
resp = requests.get('https://www.cptec.inpe.br')
content = resp.content

site = sp(content, 'html.parser')  # Transforma o conteudo do content em html
print(type(site))  # retorna <class 'bs4.BeautifulSoup'>
print(site.prettify())  # imprime o site organizadamente


# Retorna o conteudo de uma div ou tag especifica (temp. Max e Min)
post = site.find('div', attrs={'class': 'bloco-previsao d-flex flex-column text-center'})
print(post)
