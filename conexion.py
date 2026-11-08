'''CONEXION SQLITE'''

import sqlite3

def conexion_db():
    conexion = sqlite3.connect("biblioteca.db")

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            editorial TEXT,
            year INTEGER
        )
    """)

    conexion.commit()

    return conexion
