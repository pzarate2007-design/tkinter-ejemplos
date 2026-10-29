"""
02_widgets_basicos.py
Muestra los widgets (componentes) más comunes de Tkinter:
Entry, Checkbutton, Radiobutton, Combobox, Listbox, Scale, Spinbox y Button.
"""
import tkinter as tk
from tkinter import ttk  # ttk trae widgets con aspecto más moderno (Combobox)

ventana = tk.Tk()
ventana.title("Widgets básicos")
ventana.geometry("420x560")

# Variables de Tkinter: guardan el valor de un widget y se actualizan solas
nombre = tk.StringVar()
acepta = tk.BooleanVar()
color = tk.StringVar(value="Rojo")
pais = tk.StringVar()

# --- Entry: caja de texto de una línea ---
tk.Label(ventana, text="Tu nombre:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(ventana, textvariable=nombre).pack(fill="x", padx=10)

# --- Checkbutton: casilla de verificación ---
tk.Checkbutton(ventana, text="Acepto los términos", variable=acepta).pack(
    anchor="w", padx=10, pady=5
)

# --- Radiobutton: elegir UNA opción entre varias ---
tk.Label(ventana, text="Color favorito:").pack(anchor="w", padx=10)
for opcion in ("Rojo", "Verde", "Azul"):
    tk.Radiobutton(ventana, text=opcion, value=opcion, variable=color).pack(
        anchor="w", padx=25
    )

# --- Combobox: lista desplegable ---
tk.Label(ventana, text="País:").pack(anchor="w", padx=10, pady=(10, 0))
combo = ttk.Combobox(
    ventana, textvariable=pais, values=["México", "España", "Argentina", "Chile"],
    state="readonly",
)
combo.pack(fill="x", padx=10)

# --- Listbox: lista de elementos seleccionables ---
tk.Label(ventana, text="Lenguaje favorito:").pack(anchor="w", padx=10, pady=(10, 0))
lista = tk.Listbox(ventana, height=4, exportselection=False)
for lenguaje in ("Python", "JavaScript", "Java", "C++"):
    lista.insert(tk.END, lenguaje)
lista.pack(fill="x", padx=10)

# --- Scale: barra deslizante ---
tk.Label(ventana, text="Nivel de experiencia (0-10):").pack(anchor="w", padx=10, pady=(10, 0))
escala = tk.Scale(ventana, from_=0, to=10, orient="horizontal")
escala.pack(fill="x", padx=10)

# --- Spinbox: número con flechitas ---
tk.Label(ventana, text="Edad:").pack(anchor="w", padx=10)
edad = tk.Spinbox(ventana, from_=1, to=120)
edad.pack(anchor="w", padx=10)

# --- Resultado ---
resultado = tk.Label(ventana, text="", justify="left", fg="blue")
resultado.pack(pady=10)


def mostrar_resumen():
    seleccion = lista.curselection()
    lenguaje = lista.get(seleccion[0]) if seleccion else "(ninguno)"
    resultado.config(
        text=(
            f"Nombre: {nombre.get()}\n"
            f"Acepta términos: {'Sí' if acepta.get() else 'No'}\n"
            f"Color: {color.get()}\n"
            f"País: {pais.get() or '(ninguno)'}\n"
            f"Lenguaje: {lenguaje}\n"
            f"Experiencia: {escala.get()}\n"
            f"Edad: {edad.get()}"
        )
    )


tk.Button(ventana, text="Mostrar resumen", command=mostrar_resumen).pack()

ventana.mainloop()
