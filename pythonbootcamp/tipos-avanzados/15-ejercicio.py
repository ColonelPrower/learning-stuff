"""
Ejercicios
1- Eliminar espacios en blanco de un string
y devolver una lista con caracteres restantes comprension de listas DONE

2. Contar en un diccionario cuanto se repiten los caracteres
de un string ej. "lalahola" -> {"l":3,"a":3,"h":1,"o":1}
DONE

3. Ordenar las llaves de un diccionario por el valor que tienen y
devolver una lista que contiene tuplas [("a",3),("b",2)...]
DONE
4. De un listado de tuplas devolver las tuplas que tengan el mayorvalor 

5. Crear un mensaje que diga: 
    Los caracteres que mas se repiten con 4 repeticiones son:
    - C 
    - D
DONE
6. Juntar la solucion de los ejercicios para encontrar los caracteres que mas se repiten de un string
"""

mensaje = input("Cual es tu mensaje")


def eliminarespacios(mensaje):
    return [chars for chars in mensaje if chars !=" "]

mensaje = eliminarespacios(mensaje.upper())
print(mensaje)

def contardict(mensaje):
    lista = {}
    for chars in mensaje:
        if chars in lista:
            lista[chars] += 1
        else:
            lista[chars] = 1
    return lista

mensaje=contardict(mensaje)


def ordenarlista(listadict):
    lista = []
    for elemento in listadict:
        lista.append((listadict[elemento],elemento))

    lista.sort(key=lambda llave:llave[0])
    return lista
#solucion mamona
"""
return sorted(
dict.items(),key=lambda key: key[1],reverse = True
)
"""

lista_ordenada = ordenarlista(mensaje)

print(lista_ordenada)
print("Los caracteres que mas se repiten 4 veces o mas son:")
for elemento,valor in lista_ordenada:
    if elemento > 3:
        print(f"- {valor}")
