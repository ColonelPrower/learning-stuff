"""
Filas - First in First Out
"""
from collections import deque

lista = [1,2,3,4,5]
fila = deque(lista)
print(fila)

fila.popleft()
print(fila)
