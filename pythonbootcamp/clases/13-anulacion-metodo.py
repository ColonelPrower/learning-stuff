"""
Anulacion metodo, Method override
"""
class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")

class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nadar = True

    def vuela(self):
        super().vuela()
        print("vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador, pato.nadar)
