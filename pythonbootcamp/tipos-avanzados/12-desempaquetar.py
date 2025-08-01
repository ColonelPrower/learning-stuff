"""
Operador de desempaquetado
"""
lista = [1,2,3,4]
print(*lista)

lista2 = [5,6]

combinar = ["alex",*lista,lista2,"hola","mundo"]
print(combinar)
