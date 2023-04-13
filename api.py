import requests
import json
import ctypes

# Defining URLs and key for the REST API (www.coinapi.io)
cripto_url = "https://rest.coinapi.io/v1/exchangerate/{}/USD"
rates_url = "https://rest.coinapi.io/v1/exchangerate/USD/{}" 
api_key = "768E6439-1061-4146-A197-94F1AFC61779"

# Definition of the cryptocurrencies for which we want to obtain prices
cryptos = ["BTC", "ETH", "LTC"]
# Definition of the currencies to which we want to convert the crypto prices.
rates = ["ARS", "EUR"]
# For using c functions from python 
clibrary = ctypes.CDLL("./currencyconverterlib.so")

# Takes a crypto symbol and returns its price in USD
def get_crypto_price(coin): 
    url = cripto_url.format(coin)
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    price = data["rate"]
    return price

# Takes a currency symbol and returns its exchange rate against USD.
def get_rate(rate):
    url = rates_url.format(rate)
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    price = data["rate"]
    return price

# Specifying parameters and return values compatible with c
convert = clibrary.convert
convert.argtypes = [ctypes.c_float, ctypes.c_float]
convert.restype = ctypes.c_float

flag = True #stop the program when is False
while flag: 

    symbol = input("Cryptocurrency symbol: ")
    while (symbol not in cryptos) and (symbol not in [c.lower() for c in cryptos]):
        print("***ERROR: invalid cryptocurrency symbol, try again")
        symbol = input("Cryptocurrency symbol: ")
    rate = input("Currency symbol: ")
    while (rate not in rates) and (rate  not in [r.lower() for r in rates]):
        print("***ERROR: invalid currency symbol, try again")
        rate = input("Currency symbol: ")
            
    if (symbol == "BTC" or symbol == "btc") and (rate == "ARS" or rate == "ars"): 
        print("BTC price is : ", convert(get_crypto_price("BTC"), get_rate("ARS")), "ARS")
    elif (symbol == "BTC" or symbol == "btc") and (rate == "EUR" or rate == "eur"): 
        print("BTC price is: ", convert(get_crypto_price("BTC"), get_rate("EUR")), "EUR")
    elif (symbol == "ETH" or symbol == "eth") and (rate == "ARS" or rate == "ars"): 
        print("ETH price is: ", convert(get_crypto_price("ETH"), get_rate("ARS")), "ARS")
    elif (symbol == "ETH" or symbol == "eth") and (rate == "EUR" or rate == "eur"):     
        print("ETH price is: ", convert(get_crypto_price("ETH"), get_rate("EUR")), "EUR")
    elif (symbol == "LTC" or symbol == "ltc") and (rate == "ARS" or rate == "ars"): 
        print("LTC price is: ", convert(get_crypto_price("LTC"), get_rate("ARS")), "ARS")
    elif (symbol == "LTC" or symbol == "ltc") and (rate == "EUR" or rate == "eur"): 
        print("LTC price is: ", convert(get_crypto_price("LTC"), get_rate("EUR")), "EUR")

    again = input("New conversion? Y/N:  ")
    if again == "Y" or again == "y":
        flag = True
    elif again == "N" or again == "n":
        flag = False
        print("Bye!")
    