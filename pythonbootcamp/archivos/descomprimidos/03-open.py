"""
Archivos con Open
"""
from io import open

#escritura
texto = "Hola mundo!"

archivo = open("hola-mundo.txt","w")
archivo.write(texto)
archivo.close()

#lectura 

archivo = open("hola-mundo.txt","r")
texto = archivo.read()
archivo.close()
print(texto)

#lectura como lista
archivo = open("hola-mundo.txt","r")
texto = archivo.readlines()
archivo.close()
print(texto)


#with y seek
with open("hola-mundo.txt","r") as archivo:
    texto = archivo.readlines()
    print(texto)
    archivo.seek(0)
    for linea in archivo:
        print(linea)

#agregar
archivo = open("hola-mundo.txt","a+")
texto = archivo.write("chao mundo :c")
archivo.close()

#lectura y escritura
with open("hola-mundo.txt","r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0]= "Chanchito feliz la"
    archivo.writelines(texto)
