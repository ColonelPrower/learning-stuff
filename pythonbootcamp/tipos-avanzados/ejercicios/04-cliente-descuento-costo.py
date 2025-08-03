"""
Clientes con descuento 
"""

compras = {
        'Cliente1':200,
        'Cliente2':100,
        'Cliente3':180
        }

def aplicar_promocion(compras):
    promocionados = []
    comprasnew ={}
    costototal=0
    for cliente in compras:
        if compras[cliente] >= 150:
            promocionados.append(cliente)
            comprasnew[cliente] = compras[cliente]-(compras[cliente] * 0.1)
            costototal += compras[cliente] * 0.1
        else:
            comprasnew[cliente] = compras[cliente]

    return promocionados,comprasnew,costototal
print(compras)
clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)
