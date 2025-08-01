"""
Desempaquetar listas
"""

numeros = [1,2,3]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

print(primero,segundo,tercero)

primero,segundo,tercero = numeros

print(primero,segundo,tercero)

numeros = [1,2,3,4,5,6,7,8,9]
cosa,cosa2, *otros,penultimo,ultimo = numeros
print(cosa,cosa2,ultimo, penultimo,otros)
