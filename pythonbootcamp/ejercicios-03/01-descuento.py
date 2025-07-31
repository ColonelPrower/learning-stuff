"""
Aplicar descuento
100% - total
x% - ?
"""

def descuento(total,porcentaje):
    descuento = (float(total)*float(porcentaje))/100
    return float(total)-descuento


total = input("Cuanto es el total?")
porcentaje = input("Que porcentaje damos? ")
descuentofinal = descuento(total,porcentaje)
print(f"el total es: {descuentofinal}")
