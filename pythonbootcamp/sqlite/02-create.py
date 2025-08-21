"""
creando tablas
"""
import sqlite3

con = sqlite3.connect("app.db")

cursor = con.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios
               (id INTEGER primary key, nombre VARCHAR(50))
               """)
con.commit()#IMPORTANTE:Esto ejecuta la consulta sin ella no pasa nada

con.close()
