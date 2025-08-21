"""
Select one
"""
import sqlite3

with sqlite3.connect("app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchone())
