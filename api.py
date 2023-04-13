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
rates = ["ARS", "EUR", "USD"]
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

# Calls C function convert(), gets the result and prints it
def print_results(symbol, rate):
    price = convert(get_crypto_price(symbol), get_rate(rate))
    print(symbol, " price is: ", price, " ", rate)
    return

flag = True #stop the program when is False
while flag: 

    symbol = (input("Cryptocurrency symbol [BTC, ETH, LTC]: ")).upper()
    while (symbol not in cryptos):
        print("***ERROR: invalid cryptocurrency symbol, try again")
        symbol = (input("Cryptocurrency symbol [BTC, ETH, LTC]: ")).upper()
        
    rate = (input("Currency symbol [ARS, EUR, USD]: ")).upper()
    while (rate not in rates):
        print("***ERROR: invalid currency symbol, try again")
        rate = (input("Currency symbol [ARS, EUR, USD]: ")).upper()

    print_results(symbol, rate)

    again = input("New conversion? Y/N:  ")
    if again == "N" or again == "n":
        flag = False
        print("Bye!")
    