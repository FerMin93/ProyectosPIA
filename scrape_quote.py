#America Fernanda Martinez Barron
#1901395
#importando modulos
import requests
import csv
from bs4 import BeautifulSoup 
#Direccion de la pagina web
url = 'http://quotes.toscrape.com/'
#Ejecutar GET-Request
response = requests.get(url)
#Analizar sintacticamente el archivo HTML de BeatifuSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#Extarer todas las citas y autores del archivo HTML 
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
#Crear una lista de las citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
#Crear una lista de los autores 
authors = list()
for author in authors_html:
    authors.append(author.text)
#Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
#Guardar las citas y los autores en un archovo CSV en el directorio actual 
#Abriri el archivo con Excel / LibreOffice, etc.
with open('./citas_1901395.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))