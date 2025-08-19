"""
Archivos JSON (JavaScript Object Notation)
"""
import json
from pathlib import Path

#escribir json
productos = [
        {"id":1,"name":"Surfboard"},
        {"id":1,"name":"Bicicleta"},
        {"id":1,"name":"Skate"},
        ]

data = json.dumps(productos)

Path("productos.json").write_text(data)

#leer JSON
data = Path("productos.json").read_text(encoding="utf_8")
productos = json.loads(data)
print(productos)

#modificar json 
productos[0]["name"] = "Chanchito feliz"
Path("productos.json").write_text(json.dumps(productos))



