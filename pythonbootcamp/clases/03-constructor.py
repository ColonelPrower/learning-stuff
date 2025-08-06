"""
Constructor
"""
class Perro: #self tendria el valor del nombre de la instancia
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Woof!")
        print(f"tiene {self.edad} de edad")

mi_perro = Perro("Chanchito",1)
mi_perro.habla()
