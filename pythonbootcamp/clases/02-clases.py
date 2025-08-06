"""
Clase   
"""

class Perro: #Pascal Case, UpperCamelCase
    def habla(self): #funcion not, metodos yes cuando estan dentro de una clase
        print("Woof!")

mi_perro = Perro()
print(type(mi_perro))
mi_perro.habla()
print(isinstance(mi_perro,Perro))
print(isinstance(mi_perro,str))
