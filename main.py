import requests
from bs4 import BeautifulSoup

assunto = input("Digite sua cidade: ")
suba = ' '
nada = ''
acento = "'"
aa = '-'
assunto = assunto.replace(suba, aa)
assunto = assunto.replace(acento, nada)
url = f"https://www.tempo.com/{assunto}.htm"
d = requests.get(url)
sopa = BeautifulSoup(d.content, 'html.parser')
tempatual = sopa.find("span", {"class": "dato-temperatura changeUnitT"}).text
max = sopa.find("span", {"class": "maxima changeUnitT"}).text
min = sopa.find("span", {"class": "minima changeUnitT"}).text
am = sopa.find("li", {"class":"dia d2"})
max2 = am.find("span", {"class":"maxima changeUnitT"}).text
min2 = am.find("span", {"class":"minima changeUnitT"}).text
prepconselho = sopa.find("a", {"class":"modulo comentario"})
conselho = prepconselho.find("span", {"class":"datos"}).text

print(f"A previsão do tempo agora em {assunto} é de:", tempatual)
print("A máxima é:", max)
print("A mínima é:", min)
print(conselho)

print("A máxima de amanhã será:", max2)
print("A mínima de amanhã será:", min2)