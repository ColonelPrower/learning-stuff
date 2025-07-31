"""
Conversor de unidades de tiempo
seg, min, hora, dia
"""

def a_segundos(origen,cantidad,destino):
    for n in range(destino,origen):
        if n == 3: #horas a dias
            cantidad *= 24
        else:
            cantidad *= 60
    return cantidad


def de_segundos(origen,cantidad,destino):
    for n in range(origen,destino):
        if n == 3:
            cantidad /= 24
        else:
            cantidad /= 60
    return cantidad 

def convertir_tiempo(origen,cantidad,destino):
    if origen < destino:
        return de_segundos(origen,cantidad,destino)
    elif origen > destino:
        return a_segundos(origen,cantidad,destino)
    return "error"

print("Selecciona la unidad:")
print("1 - segundos")
print("2 - minutos")
print("3 - horas")
print("4 - dias")

origen = input("Unidad origen: ")
cantidad = input("ingresa la cantidad:")
destino = input("Unidad destino: ")

print(convertir_tiempo(int(origen),int(cantidad),int(destino)))
