"""
Tipos de Excepciones
"""
try:
    n1 = int(input("Ingresa numero: "))
except ValueError as e:
    print("Ingrese un valor numerico")
except NameError as e:
    print("ocurrio un error")

