"""
Decorador de propiedades
"""
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property 
    def nombre(self):
        print("pasa al getter")
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        print("pasa al setter")
        if nombre.strip():
            self.__nombre = nombre
        return

perro = Perro("Choclo")
print(perro.nombre)
