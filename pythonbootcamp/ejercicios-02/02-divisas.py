"""
Convertidor de divisas
"""

usdeur = 0.95
usdmxn = 20.28
eurmxn = 21.36

"""
usd - eur 
usd - mxn 

eur - usd 
eur - mxn 

mxn - usd 
mxn - eur 

"""

cantidad = int(input("ingresa Cantidad"))
moneda = input("ingresa Moneda").upper()

if moneda not in ["USD","MXN","EUR"]:
    print("Moneda no valida")
else:
    print(f"{cantidad} {moneda} son:")
    match moneda:
        case "USD":
            print(f"{cantidad*usdmxn} MXN")
            print(f"{cantidad*usdeur} EUR")
        case "MXN":
            print(f"{cantidad/usdmxn} USD")
            print(f"{cantidad/eurmxn} EUR")
        case "EUR":
            print(f"{cantidad/usdeur} USD")
            print(f"{cantidad*eurmxn} MXN")

