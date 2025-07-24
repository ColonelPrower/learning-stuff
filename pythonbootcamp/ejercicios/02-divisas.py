#Aproximaciones del 2025
cantidad = int(input("Ingresa cantidad en pesos MXN: "))
usd = cantidad / 20
eur = cantidad / 21
gbp = cantidad / 25
jpy = cantidad / 0.13

print(f"${cantidad} MXN equivalen a:")
print(f"USD: {usd}")
print(f"EUR: {eur}")
print(f"GBP: {gbp}")
print(f"JPY: {jpy}")