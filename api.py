import requests
import json
import ctypes

# Define la URL base de la API REST y la clave de la API
url_base = "https://rest.coinapi.io/v1/exchangerate/{}/USD"
api_key = "768E6439-1061-4146-A197-94F1AFC61779"

# Define las criptomonedas para las que desea obtener los precios
cryptos = ["BTC", "ETH", "LTC"]

# Crea una lista vacía para almacenar los precios
prices = []

# Realiza una solicitud HTTP GET a la API REST para cada criptomoneda y almacena el precio en la lista de precios
for crypto in cryptos:
    url = url_base.format(crypto)
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    price = data["rate"]
    prices.append(price)

# Imprime los precios de las criptomonedas
print("Precio de Bitcoin:", prices[0], "USD")
print("Precio de Ethereum:", prices[1], "USD")
print("Precio de Litecoin:", prices[2], "USD")