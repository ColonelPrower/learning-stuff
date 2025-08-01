"""
ordenar listas
"""
numeros=[2,5,1,0,53,23,11]

numeros2 = numeros

print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

numeros3 = sorted(numeros2, reverse=True)
print(numeros3) #crea una nueva lista

usuarios = [[4,"Chanchito"],[1,"Felipe"],[5,"Pulga"]]
usuarios.sort()
print(usuarios)

def ordena(elemento):
    return elemento[1]

#usuarios.sort(key=ordena)
usuarios.sort(key=lambda parametros:parametros[0],reverse=True)
print(usuarios)
