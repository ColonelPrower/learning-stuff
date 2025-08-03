"""
Dado
"""
import random

def tirar_dados(n):
    resultados = [0]*6

    for _ in range(n):
        resultado = random.randint(1,6)
        resultados[resultado - 1] += 1
    if n == 1:
        print(f"Salió la cara: {resultado}")
    else:
        for i in range(6):
            porcentaje = (resultados[i]/n) * 100
            print(f"Cara {i + 1}: {porcentaje:.2f}%")

tirar_dados(10)

