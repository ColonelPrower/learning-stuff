"""
Web Scrapping
"""

import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

resp = requests.get(url)

texto = resp.text

soup = BeautifulSoup(texto,"html.parser")

preguntas = soup.select(".s-post-summary")

for preg in preguntas:
    titulo = preg.select_one(".s-link").get_text()
    usuario = preg.select_one(".s-user-card--link").get_text()
    print(f"{usuario.strip()} - Titulo: \n{titulo}")
