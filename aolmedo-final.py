'''====== PROYECTO FINAL ========='''

import time
import tkinter as tk
from tkinter import ttk, messagebox

from crud import (
    crear_libro,
    leer_libros,
    buscar_libro,
    borrar_libro,
    actualizar_libro
)

# CONFIGURACIÓN DE LA VENTANA

ventana = tk.Tk()
ventana.title("CRUD - Biblioteca")
ventana.geometry("950x650")
ventana.minsize(800, 550)
ventana.configure(bg="ivory3")

# FUNCIONES

def limpiar_campos():
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_editorial.delete(0, tk.END)
    entrada_year.delete(0, tk.END)

    tabla.selection_remove(tabla.selection())

def obtener_datos():

    titulo = entrada_titulo.get().strip()
    autor = entrada_autor.get().strip()
    editorial = entrada_editorial.get().strip()
    year = entrada_year.get().strip()

    # Validar campos vacíos
    if not titulo or not autor or not editorial or not year:
        messagebox.showwarning(
            "Datos incompletos",
            "Todos los campos son obligatorios."
        )
        return None

    # Validar que el año contenga números
    if not year.isdigit():
        messagebox.showwarning(
            "Dato incorrecto",
            "El año debe contener solamente números."
        )
        return None

    year = int(year)

    return titulo, autor, editorial, year


def cargar_libros(datos=None):

    if datos is None:
        datos = leer_libros()

    # Limpiar tabla
    for elemento in tabla.get_children():
        tabla.delete(elemento)

    # Cargar registros
    for libro in datos:
        tabla.insert(
            "",
            tk.END,
            iid=str(libro[0]),
            values=libro
        )


def alta_libro():

    datos = obtener_datos()

    if datos is None:
        return

    crear_libro(*datos)

    messagebox.showinfo(
        "Alta",
        "Libro registrado correctamente."
    )

    cargar_libros()
    limpiar_campos()


def consultar_libros():

    cargar_libros()
    limpiar_campos()


def limpiar_entradas():

    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_editorial.delete(0, tk.END)
    entrada_year.delete(0, tk.END)


def seleccionar_libro(event=None):

    seleccion = tabla.selection()

    if not seleccion:
        return

    libro = tabla.item(seleccion[0], "values")

    limpiar_entradas()

    entrada_titulo.insert(0, libro[1])
    entrada_autor.insert(0, libro[2])
    entrada_editorial.insert(0, libro[3])
    entrada_year.insert(0, libro[4])


def editar_libro():

    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning(
            "Editar",
            "Seleccioná un libro de la tabla."
        )
        return

    datos = obtener_datos()

    if datos is None:
        return

    id_libro = int(seleccion[0])

    actualizar_libro(id_libro, *datos)

    messagebox.showinfo(
        "Editar",
        "Libro actualizado correctamente."
    )

    cargar_libros()
    limpiar_campos()


def eliminar_libro():

    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning(
            "Baja",
            "Seleccioná un libro de la tabla."
        )
        return

    id_libro = int(seleccion[0])

    confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        "¿Estás seguro de eliminar el libro seleccionado?"
    )

    if confirmar:

        borrar_libro(id_libro)

        messagebox.showinfo(
            "Baja",
            "Libro eliminado correctamente."
        )

        cargar_libros()
        limpiar_campos()


def buscar_libros():

    titulo = entrada_busqueda.get().strip()

    if not titulo:
        cargar_libros()
    else:
        resultados = buscar_libro(titulo)
        cargar_libros(resultados)


def reloj_hora():

    reloj.config(text=time.strftime("%H:%M:%S"))

    ventana.after(1000, reloj_hora)

def salir_aplicacion():

    confirmar = messagebox.askyesno(
        "Salir de la aplicación",
        "¿Estás seguro que querés salir de la aplicación?"
    )

    if confirmar:
        ventana.destroy()


# TÍTULO Y RELOJ

titulo = tk.Label(
    ventana,
    text="SISTEMA CRUD PARA BIBLIOTECA",
    bg="ivory3",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=15)

reloj = tk.Label(
    ventana,
    text="",
    bg="ivory3",
    font=("Arial", 12)
)

reloj.pack(anchor="ne", padx=20)

reloj_hora()

# FORMULARIO DE LIBROS

frame_formulario = tk.LabelFrame(
    ventana,
    text="Datos del libro",
    bg="ivory3",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

frame_formulario.pack(fill="x", padx=20, pady=10)


tk.Label(frame_formulario, text="Título:", bg="ivory3").grid(
    row=0, column=0, sticky="w", padx=5, pady=5
)

entrada_titulo = tk.Entry(frame_formulario, width=35)
entrada_titulo.grid(row=0, column=1, padx=5, pady=5)


tk.Label(frame_formulario, text="Autor:", bg="ivory3").grid(
    row=0, column=2, sticky="w", padx=5, pady=5
)

entrada_autor = tk.Entry(frame_formulario, width=30)
entrada_autor.grid(row=0, column=3, padx=5, pady=5)


tk.Label(frame_formulario, text="Editorial:", bg="ivory3").grid(
    row=1, column=0, sticky="w", padx=5, pady=5
)

entrada_editorial = tk.Entry(frame_formulario, width=35)
entrada_editorial.grid(row=1, column=1, padx=5, pady=5)


tk.Label(frame_formulario, text="Año:", bg="ivory3").grid(
    row=1, column=2, sticky="w", padx=5, pady=5
)

entrada_year = tk.Entry(frame_formulario, width=30)
entrada_year.grid(row=1, column=3, padx=5, pady=5)

# BOTONES CRUD

frame_botones = tk.Frame(ventana, bg="ivory3")
frame_botones.pack(pady=10)

crear = tk.Button(
    frame_botones,
    text="ALTA",
    bg="lightblue",
    width=15,
    command=alta_libro
)
crear.grid(row=0, column=0, padx=8)

leer = tk.Button(
    frame_botones,
    text="CONSULTA",
    bg="lightgreen",
    width=15,
    command=consultar_libros
)
leer.grid(row=0, column=1, padx=8)

actualizar = tk.Button(
    frame_botones,
    text="EDITAR",
    bg="lightyellow",
    width=15,
    command=editar_libro
)
actualizar.grid(row=0, column=2, padx=8)

borrar = tk.Button(
    frame_botones,
    text="BAJA",
    bg="lightpink",
    width=15,
    command=eliminar_libro
)
borrar.grid(row=0, column=3, padx=8)

# BÚSQUEDA

frame_busqueda = tk.Frame(ventana, bg="ivory3")
frame_busqueda.pack(pady=10)

tk.Label(
    frame_busqueda,
    text="Buscar por título:",
    bg="ivory3",
    font=("Arial", 11)
).grid(row=0, column=0, padx=5)

entrada_busqueda = tk.Entry(frame_busqueda, width=35)
entrada_busqueda.grid(row=0, column=1, padx=5)

buscar = tk.Button(
    frame_busqueda,
    text="BUSCAR",
    bg="orange",
    width=15,
    command=buscar_libros
)
buscar.grid(row=0, column=2, padx=5)

entrada_busqueda.bind("<Return>", lambda event: buscar_libros())

# TABLA DE LIBROS

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)

columnas = ("id", "titulo", "autor", "editorial", "year")

tabla = ttk.Treeview(
    frame_tabla,
    columns=columnas,
    show="headings",
    selectmode="browse"
)

tabla.heading("id", text="ID")
tabla.heading("titulo", text="Título")
tabla.heading("autor", text="Autor")
tabla.heading("editorial", text="Editorial")
tabla.heading("year", text="Año")

tabla.column("id", width=50, anchor="center")
tabla.column("titulo", width=220)
tabla.column("autor", width=160)
tabla.column("editorial", width=180)
tabla.column("year", width=80, anchor="center")

scrollbar = ttk.Scrollbar(
    frame_tabla,
    orient="vertical",
    command=tabla.yview
)

tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tabla.bind("<<TreeviewSelect>>", seleccionar_libro)

# BOTÓN SALIR

boton_salir = tk.Button(
    ventana,
    text="SALIR DE LA APLICACIÓN",
    bg="red",
    fg="white",
    font=("Arial", 10),
    width=25,
    height=2,
    command=salir_aplicacion
)

boton_salir.pack(pady=10)

cargar_libros()

ventana.mainloop()