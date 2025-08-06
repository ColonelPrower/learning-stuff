"""
Metodos Magicos
__init__
__main__
__str__
"""

class Perro:
    def __init__(self,nombre,edad): #<- metodo magico
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self): #destructor
        print(f"Chao perro {self.nombre} :c ")

    def habla(self):
        print("Guau!")

perro = Perro("chanchito",1)

print(perro)
del perro

