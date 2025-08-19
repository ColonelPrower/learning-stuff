"""
Lectura y escritura de archivos
"""
from pathlib import Path

archivo = Path("archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")

texto.insert(0,"hola mundo!")
archivo.write_text("\n".join(texto),"utf-8")
print(texto)
