

import requests
from bs4 import BeautifulSoup

url_base = "https://bleach.fandom.com/es/wiki/"
url_armas = "https://bleach.fandom.com/es/wiki/Lista_de_Armas"
url_hollows = "https://bleach.fandom.com/es/wiki/Hollow#Menos"
url_quincy = "https://bleach.fandom.com/es/wiki/Lista_de_Quincy"

respuesta = requests.get(url_armas)
if respuesta.status_code != 200:
        raise ValueError("No se pudo obtener la información de la página")
soup = BeautifulSoup(respuesta.text, "html.parser")

h3 = soup.find('span', {'id': 'Zanpaku-t.C5.8D_de_Shinigamis_y_Visored'})
tabla = h3.find_next('table')

shiningamis = []
for fila in tabla.find_all('tr')[2:]:
    columnas = fila.find_all('td')
    if len(columnas) >=3:
        nombre = columnas[1].text.strip()
        zanpakuto = columnas[0].text.strip()
        bankai = columnas[2].text.strip()
        shiningamis.append((nombre, zanpakuto, bankai))

# imprimo los nombres de las armas y sus shinigamis
print("Nombre de las armas y sus shinigamis:")
for shinigami in shiningamis:
    # numero de shinigamis para menu
    print(f"{shiningamis.index(shinigami) + 1}. {shinigami[0]}")
    print(f"Zanpakuto: {shinigami[1]}")
    print(f"Bankai: {shinigami[2]}")
    print("")

#captura el numero de shinigami
numero_shinigami = int(input("Ingrese el numero del shinigami que desea ver: ")) - 1
shinigami_seleccionado = shiningamis[numero_shinigami]
print(shinigami_seleccionado)

#url del shiningami seleccionado
url_shinigami = url_base + shinigami_seleccionado[0].replace(" ", "_")
print(url_shinigami)

#capturar respuesta para el shinigami seleccionado
respuesta = requests.get(url_shinigami)
if respuesta.status_code != 200:
        raise ValueError("No se pudo obtener la información de la página")

soup = BeautifulSoup(respuesta.text, 'html.parser') #parsear la respuesta de la pagina
sumario = soup.find('div', {'id': 'toc'})
descripcion = sumario.find_previous('p').text.strip()
print(descripcion)
