"""
comprension de listas
"""
usuarios = [[4,"Chanchito"],[1,"Felipe"],[5,"Pulga"]]

nombres = []

for usuario in usuarios:
    nombres.append(usuario[1])
print(nombres)

nombres.clear()
nombres = [usuario[1] for usuario in usuarios]
print(nombres)
#filtrar
nombres.clear()
#nombres = [usuario for usuario in usuarios if usuario[0] > 2]
nombres = [usuario[1] for usuario in usuarios if usuario[0] > 2]
print(nombres)

nombres.clear()
nombres = list(map(lambda usuario:usuario[1], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[0]>2, usuarios))
print(menosUsuarios)
