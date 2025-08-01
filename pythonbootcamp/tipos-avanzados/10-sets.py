"""
Sets, grupos o conjuntos
no tienen items repetidos y no estan ordenados
"""

primer = {1,1,2,2,3,4}
#print(primer)
#primer.add(5)
#primer.remove(1)
#print(primer)

segundo = [3,4,5]
segundo = set(segundo)
print(segundo)

print(primer | segundo) #Union
print(primer & segundo) #Interseccion
print(primer - segundo) #diferencia
print(primer ^ segundo) #diferencia simetrica

