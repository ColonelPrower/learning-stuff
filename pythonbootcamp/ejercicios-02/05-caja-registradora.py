"""
Caja registradora
"""

total = 0.0

while True:
    cantidad = input("Ingresa cantidad, \"fin\" para finalizar: ")
    if not cantidad or cantidad.lower() == "fin":
        print("Adios")
        break
    total += float(cantidad)
    print(f"El total es: {total:.2f}")
