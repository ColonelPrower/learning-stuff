"""
Metodos de clase
"""

class Perro:
    patas = 4
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("chanchito feliz", 4)

perro = Perro.factory()
print(perro.edad, perro.nombre)


