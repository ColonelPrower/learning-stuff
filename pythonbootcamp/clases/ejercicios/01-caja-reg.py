"""
Caja registradora
"""

class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def add_producto(self,producto,precio):
        self.productos.append({"nombre":producto,"precio":precio})
        print(f"{producto} agregado")

    def get_total(self):
        total = 0
        for producto in self.productos:
            total += producto['precio']
        return total

    def get_productos(self):
        for producto in self.productos:
            print(producto['nombre'],producto['precio'])

    def calcular_cambio(self,dinero):
        total = self.get_total()
        if dinero < total:
            print("saldo insuficiente")
        else:
            cambio = dinero - total
            print(f"su cambio {cambio}")
            self.productos.clear()


cliente = CajaRegistradora()
cliente.add_producto("Manzana",0.5)
cliente.add_producto("Pan",1.0)
cliente.get_total()
cliente.get_productos()
cliente.calcular_cambio(1)
cliente.calcular_cambio(2)
cliente.get_productos()

