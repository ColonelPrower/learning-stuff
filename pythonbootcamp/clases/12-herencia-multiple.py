"""
Herencia Multiple
Buena practica tratar que los metodos heredados no se repitan 
"""
class Animal:
    def comer(self):
        print("comiendo")

class Perro:
    def pasear(self):
        print("pasenando")

class Chanchito(Perro, Animal): #<--Herencia Multiple
    def programar(self):
        print("programando")

