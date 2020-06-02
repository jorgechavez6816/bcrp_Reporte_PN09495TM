#Obtención automática de tablas del BCRP - PN09495TM
#Operaciones cambiarias del BCRP con las empresas bancarias (millones US$) - Al Contado - Compras

#01. Importación de librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN09495TM/html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#02. Obtención de fecha
eq = soup.find_all('td', class_='periodo')
equipos = list()
count = 0
for i in eq:
    if count <148:
        equipos.append(i.text.strip("\n"))
    else:
        break
    count +=1
    
#03. Obtención demontos 
pt = soup.find_all('td', class_='dato')
puntos = list()
count = 0
for i in pt:
    if count <148:
        puntos.append(i.text.strip("\n"))
    else:
        break
    count +=1

#04. Creación de archivo de salida
df = pd.DataFrame({'Fecha': equipos, 'Millones_US': puntos}, index=list(range(1,149)))
df.to_csv('C:\\Users\\Intel\\Documents\\Mis documentos IDEA\\Samples\\Archivos fuente.ILB\\Reporte_PN09495TM.csv', encoding='utf-8')
