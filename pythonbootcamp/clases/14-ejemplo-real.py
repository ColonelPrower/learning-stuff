"""
Ejemplo real
"""
class Model():
    tabla = False
    def __init__(self):
        if not self.tabla:
            print("Error, define una tabla")

    def guardar(self):
        print(f"Guardando en {self.tabla} en BD")

    @classmethod
    def buscar_x_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()
usuario.guardar()
Usuario.buscar_x_id(123)
