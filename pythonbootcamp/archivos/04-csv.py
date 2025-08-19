"""
Archivos csv
"""
import csv
import os
#escribir
with open("archivo.csv","w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id","user_id","text"])
    writer.writerow([1000,1,"este es un tweet"])
    writer.writerow([1001,2,"otro tweet"])

#leer
with open("archivo.csv") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)

#actualizar
with open("archivo.csv") as r, open("archivo-temp.csv","w") as temp:
    reader = csv.reader(r)
    writer = csv.writer(temp)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000,1,"texto modificado"])
        else:
            writer.writerow(linea)#hay que pasar el texto actual al temporal
    os.remove("archivo.csv")
    os.rename("archivo-temp.csv","archivo.csv" )
