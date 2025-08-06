"""
Polimorfismo
"""

class Usuario:
    def guardar(self):
        print("Guardando en BD")

class Sesion:
    def guardar(self):
        print("guardando en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()
guardar([sesion,usuario])
