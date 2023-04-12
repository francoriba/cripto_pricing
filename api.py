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
somecripto_somerate = clibrary.somecripto_somerate
somecripto_somerate.argtypes = [ctypes.c_float, ctypes.c_float]
somecripto_somerate.restype = ctypes.c_float

print(get_rate("ARS"))

flag = True
while flag: 

    symbol = input("Simbolo de criptomoneda: ")
    while (symbol not in cryptos) and (symbol not in [c.lower() for c in cryptos]):
        print("***ERROR: el símbolo de criptomoneda no es válido, intente nuevamente")
        symbol = input("Simbolo de criptomoneda: ")
    rate = input("Moneda: ")
    while (rate not in rates) and (rate  not in [r.lower() for r in rates]):
        print("***ERROR: El símbolo de moneda no es válido, intente nuevamente")
        rate = input("Simbolo de moneda: ")
            
    if (symbol == "BTC" or symbol == "btc") and (rate == "ARS" or rate == "ars"): 
        print("El precio del BTC es: ", somecripto_somerate(get_crypto_price("BTC"), get_rate("ARS")), "ARS")
    elif (symbol == "BTC" or symbol == "btc") and (rate == "EUR" or rate == "eur"): 
        print("El precio del BTC es: ", somecripto_somerate(get_crypto_price("BTC"), get_rate("EUR")), "EUR")
    elif (symbol == "ETH" or symbol == "eth") and (rate == "ARS" or rate == "ars"): 
        print("El precio del ETH es: ", somecripto_somerate(get_crypto_price("ETH"), get_rate("ARS")), "ARS")
    elif (symbol == "ETH" or symbol == "eth") and (rate == "EUR" or rate == "eur"):     
        print("El precio del ETH es: ", somecripto_somerate(get_crypto_price("ETH"), get_rate("EUR")), "EUR")
    elif (symbol == "LTC" or symbol == "ltc") and (rate == "ARS" or rate == "ars"): 
        print("El precio del LTC es: ", somecripto_somerate(get_crypto_price("LTC"), get_rate("ARS")), "ARS")
    elif (symbol == "LTC" or symbol == "ltc") and (rate == "EUR" or rate == "eur"): 
        print("El precio del LTC es: ", somecripto_somerate(get_crypto_price("LTC"), get_rate("EUR")), "EUR")

    again = input("Nueva consulta? Y/N:  ")
    if again == "Y" or again == "y":
        flag = True
    elif again == "N" or again == "n":
        flag = False
        print("Matanga dijo la changa")
    