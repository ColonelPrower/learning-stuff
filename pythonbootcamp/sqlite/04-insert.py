"""
Insert
"""
import sqlite3

with sqlite3.connect("app.db") as con:
    cursor = con.cursor()
    cursor.execute("insert into usuarios values(?,?)",
                   (1,"HolaMundo"))#Esto evita un sql injection :O
