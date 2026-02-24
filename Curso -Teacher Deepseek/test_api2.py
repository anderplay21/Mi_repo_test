import requests
from bs4 import BeautifulSoup

url = "https://www.eltiempo.com/"
response = requests.get(url)

# Comprobamos si se descargó bien la página
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    # Buscamos los titulares (esto puede cambiar según la página)
    titulares = soup.find_all('h2', class_='title')  # Cambia 'h2' y 'title' según la estructura real de la página

    print("Titulares encontrados:")
    for t in titulares[:10]:  # solo los primeros 10
        print("-", t.get_text(strip=True))
else:
    print("No se pudo acceder a la página:", response.status_code)
