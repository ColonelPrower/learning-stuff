"""
Propiedades de clase
"""

class Perro:
    patas = 4
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

mi_perro = Perro("Chanchito",1)
mi_perro = Perro("Felipe",1)
print(Perro.patas)
Perro.patas = 3
print(mi_perro.patas)
mi_perro.patas = 5
print(mi_perro.patas)
print(Perro.patas)
