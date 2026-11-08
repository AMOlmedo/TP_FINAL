from conexion import conexion_db


def crear_libro(titulo, autor, editorial, year):
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO libros (titulo, autor, editorial, year)
        VALUES (?, ?, ?, ?)
        """,
        (titulo, autor, editorial, year)
    )

    conexion.commit()

    id_libro = cursor.lastrowid     
#lastrowid  permite conocer el identificador asignado por SQLite al último registro insertado mediante ese cursor
    conexion.close()

    return id_libro    


def leer_libros():
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libros")

    datos = cursor.fetchall()

    conexion.close()

    return datos


def actualizar_libro(id_libro, titulo, autor, editorial, year):
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE libros
        SET titulo=?, autor=?, editorial=?, year=?
        WHERE id=?
        """,
        (titulo, autor, editorial, year, id_libro)
    )

    conexion.commit()
    conexion.close()


def borrar_libro(id_libro):
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM libros WHERE id=?",
        (id_libro,)
    )

    conexion.commit()
    conexion.close()


def buscar_libro(titulo):
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT * FROM libros
        WHERE titulo LIKE ?
        """,
        (f"%{titulo}%",)
    )

    resultado = cursor.fetchall()

    conexion.close()

    return resultado