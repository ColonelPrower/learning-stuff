"""
Lista de tareas
"""
tareas =[
        {'id':1,"desc":"lavar los platos"},
        {'id':2,"desc":"sacar la basura"},
        {'id':3,"desc":"Limpiar el baño"},
        {'id':4,"desc":"Hacer la cama"},
        {'id':5,"desc":"Cocina cena"},
        {'id':6,"desc":"Pasear al perro"},
        {'id':7,"desc":"Hacer compras"},
        {'id':8,"desc":"Planchar"},
        {'id':9,"desc":"Regar plantas"},
        {'id':10,"desc":"Lavar el coche"},
        ]



def buscarxid(n):
    for i in tareas:
        if i['id']==n:
            return i['desc']
    return "no encontrado"

def buscarxdesc(desc):
    print("Tareas encontradas:")
    for i in tareas:
        if desc.lower() in i['desc'].lower():
            print(i["id"], i['desc'])

buscar = input("1 ID 2 por desc ")
if int(buscar) == 1:
    print(buscarxid(int(input("ingresa el ID: "))))
elif int(buscar) == 2:
    buscarxdesc(input("Ingresa la descripcion o parte de ella: "))
else:
    print("no valido")
