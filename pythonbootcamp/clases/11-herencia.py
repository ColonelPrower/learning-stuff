"""
Herencia
"""
class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("pasenando")

class Chanchito(Perro): #Herencia multinivel no usar mas de 2 niveles
    def programar(self):
        print("programando")

perro = Perro()
perro.comer()

chanchito = Chanchito()
chanchito.pasear()
