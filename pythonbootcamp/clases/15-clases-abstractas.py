"""
Clases Abstractas
"""
from abc import ABC, abstractmethod

class Model(ABC):
    
    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardando en {self.tabla} en BD")

    @classmethod
    def buscar_x_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

model = Usuario()
Usuario.buscar_x_id(123)
