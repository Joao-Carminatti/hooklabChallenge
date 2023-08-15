#Importando as bibliotecas
import requests
from bs4 import BeautifulSoup
import csv

#Fazendo o download da página!
url = "https://www.reddit.com/r/programming/"
response = requests.get(url)
html = response.text

#Analisando o código HTML da página!
soup = BeautifulSoup(html, "html.parser")

#Pega todos os posts da página!
posts = soup.find_all("shreddit-post")

#Cria lista que irá armazenar os dados
data = []

#loop para pegar as informações necessárias das 3 primeiras postagens
for post in posts[0:3]:
    title = post["post-title"]
    upvotes = post["score"]
    link = post["content-href"]

    data.append([title ,upvotes, link])

#Criando o arquivo csv com as informações
with open("informations_reddit.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Título", "Upvotes", "Link"])
    writer.writerows(data)
