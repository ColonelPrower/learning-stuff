"""
Jerarquia de clases para vehiculos 
"""

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return {"Marca":self.marca,"Modelo":self.modelo}

class Coche(Vehiculo):
    def descripcion(self):
        return f"Coche - {super().descripcion()}"

class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto - {super().descripcion()}"

class Bicicleta(Vehiculo):
    def descripcion(self):
        return f"Bicicleta - {super().descripcion()}"

versa = Coche("Nissan","Versa")
yamaha = Moto("Yamaha","MT-07")
giant = Bicicleta("Giant","Escape 3")

print(versa.descripcion())
print(yamaha.descripcion())
print(giant.descripcion())

