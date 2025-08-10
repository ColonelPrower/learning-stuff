"""
Invocar excepciones customizadas
"""
class MiError(Exception):
    """Esta clase representa mi error"""
    def __init__(self,mensaje,codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - code: {self.codigo}"



def division(n = 0):
    if n == 0:
        raise MiError("No se puede dividir por 0, tas loco viteh",512)
    return 5 / n

try:
    division()
except MiError as e:
    print("hubo un error:",e.codigo,e.mensaje)
    print(e)
