"""
Archivos comprimidos
"""
from pathlib import Path
from zipfile import ZipFile

with ZipFile("comprimidos.zip","w") as zip:
    for path in Path().rglob("*.*"): #todo lo que esta dentro de esta carpeta
        print(path)
        if str(path) != "comprimidos.zip":
            zip.write(path)

#leer zip
with ZipFile("comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("06-comprimidos.py")
    print(
            info.file_size,
            info.compress_size
            )
    zip.extractall("descomprimidos")
