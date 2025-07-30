"""
alcance, scope
"""
saludo = "Hola Global" #Mala practica usar variables globales
def saludar():
    saludo = "Hola mundo"
    print(saludo)

def saludaChanchito():
    saludo = "Hola chanchito"
    print(saludo)

def saludo3():
    global saludo3
    print(saludo3)

saludar()
print(saludo)
saludaChanchito()
saludo3()
