import requests

def obtener_clima(ciudad, api_key):
    """
    Obtiene el clima actual de una ciudad utilizando la API de OpenWeatherMap.

    :param ciudad: Nombre de la ciudad.
    :param api_key: Clave de la API de OpenWeatherMap.
    :return: Diccionario con los datos del clima o un mensaje de error.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        if datos.get("cod") != 200:
            return f"Error: {datos.get('message', 'No se pudo obtener el clima.')}"
        return datos
    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {e}"

def mostrar_clima(datos):
    """
    Muestra los datos del clima de forma legible.

    :param datos: Diccionario con los datos del clima.
    """
    if isinstance(datos, str):
        print(datos)
    else:
        print(f"Ciudad: {datos['name']}, {datos['sys']['country']}")
        print(f"Clima: {datos['weather'][0]['description']}")
        print(f"Temperatura: {datos['main']['temp']}°C")
        print(f"Sensación térmica: {datos['main']['feels_like']}°C")
        print(f"Humedad: {datos['main']['humidity']}%")
        print(f"Velocidad del viento: {datos['wind']['speed']} m/s")

def main():
    """
    Función principal de la aplicación.
    """
    print("Bienvenido al notificador del clima.")
    api_key = input("Por favor, ingresa tu API Key de OpenWeatherMap: ")
    while True:
        ciudad = input("Ingresa el nombre de una ciudad (o escribe 'salir' para terminar): ")
        if ciudad.lower() == 'salir':
            print("Gracias por usar el notificador del clima. ¡Adiós!")
            break
        datos_clima = obtener_clima(ciudad, api_key)
        mostrar_clima(datos_clima)

if __name__ == "__main__":
    main()