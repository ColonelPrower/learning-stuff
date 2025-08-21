"""
creando tablas
"""
import sqlite3

with sqlite3.connect("app.db") as con:
    cursor = con.cursor()
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios
               (id INTEGER primary key, nombre VARCHAR(50))
               """)
    #con with ya no es necesario commit y cerrar la base
