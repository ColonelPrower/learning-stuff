"""
inyeccion de dependencias
"""
from pathlib import Path

path = Path()

paths = [p for p in path.iterdir() if p.is_dir()]
dependencias = {
        "db":"base de datos",
        "api":"esta es la api",
        "graphql":"este es un graphql"
        }

def load(p):
    # print(str(p))
    paquete = __import__(str(p).replace("/","."))
    try:
        paquete.init(**dependencias)
    except Exception as e:
        print("el paquete no existe")

list(map(load, paths))
