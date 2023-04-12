import requests
import json
import ctypes

# Definimos las URLs y clave de la API REST (www.coinapi.io)
cripto_url = "https://rest.coinapi.io/v1/exchangerate/{}/USD" 
rates_url = "https://rest.coinapi.io/v1/exchangerate/USD/{}" 
api_key = "768E6439-1061-4146-A197-94F1AFC61779"

# Definimos las criptomonedas para las que desea obtener los precios
cryptos = ["BTC", "ETH", "LTC"]
#Definimos las divisas a las que queremos convertir los precios de las cripto
rates = ["ARS", "EUR"]

clibrary = ctypes.CDLL("./currencyconverterlib.so")

#Recibe una cripto como arg y retorna su precio
def get_crypto_price(coin): 
    #while coin not in cryptos:
    #    print("La cripto solicitada no es válida, intente nuevamente")
    url = cripto_url.format(coin)
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    price = data["rate"]
    return price

#Recibe una moneda como arg y retorna su cotización frente a los usd
def get_rate(rate):
    #while rate not in rates:
    #    print("La cotización solicitada no es válida, intente nuevamente")
    url = rates_url.format(rate)
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    price = data["rate"]
    return price

#Especificamos parametros y valores de retorno compatibles con c
btc_ars = clibrary.btc_ars
btc_ars.argtypes = [ctypes.c_float, ctypes.c_float]
btc_ars.restype = ctypes.c_float

btc_eur = clibrary.btc_eur
btc_eur.argtypes = [ctypes.c_float, ctypes.c_float]
btc_eur.restype = ctypes.c_float

eth_ars = clibrary.eth_ars
eth_ars.argtypes = [ctypes.c_float, ctypes.c_float]
eth_ars.restype = ctypes.c_float

eth_eur = clibrary.eth_eur
eth_eur.argtypes = [ctypes.c_float, ctypes.c_float]
eth_eur.restype = ctypes.c_float

ltc_ars = clibrary.ltc_ars
ltc_ars.argtypes = [ctypes.c_float, ctypes.c_float]
ltc_ars.restype = ctypes.c_float

ltc_eur = clibrary.ltc_eur
ltc_eur.argtypes = [ctypes.c_float, ctypes.c_float]
ltc_eur.restype = ctypes.c_float

print("El precio del BTC es: ", btc_ars(get_crypto_price("BTC"), get_rate("ARS")), "ARS")
print("El precio del BTC es: ", btc_eur(get_crypto_price("BTC"), get_rate("EUR")), "EUR")
print("El precio del ETH es: ", eth_ars(get_crypto_price("ETH"), get_rate("ARS")), "ARS")
print("El precio del ETH es: ", eth_eur(get_crypto_price("ETH"), get_rate("EUR")), "EUR")
print("El precio del LTC es: ", ltc_ars(get_crypto_price("LTC"), get_rate("ARS")), "ARS")
print("El precio del LTC es: ", ltc_eur(get_crypto_price("LTC"), get_rate("EUR")), "EUR")