# Separador de miles y decimales de 4

# $ python bitcoin.py                                                             
# Missing command-line argument  

# $ python bitcoin.py cat                                                         
# Command-line argument is not a number 

# $ python bitcoin.py 1                                                           
# $38,761.0833 

# python bitcoin.py 1.5
# $58,141.6249 

import requests
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    numero = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = os.getenv("COINCAP_API_KEY")
try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    response.raise_for_status()
except requests.RequestException:
    sys.exit("Error al consultar la API")

o = response.json()

data = o["data"]
price = data["priceUsd"]

resultado = numero * float(price)
print(f"${resultado:,.4f}")