"""
Clientes 
"""

compras = {
        'Cliente1':200,
        'Cliente2':100,
        'Cliente3':180
        }

def aplicar_promocion(compras):
    promocionados = []
    for cliente in compras:
        if compras[cliente] >= 150:
            promocionados.append(cliente)
    return promocionados

clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)
