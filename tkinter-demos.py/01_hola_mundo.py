"""
01_hola_mundo.py
Tu primera ventana con Tkinter: ventana, etiqueta (Label) y botón (Button).
"""
import tkinter as tk

# 1) Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo con Tkinter")
ventana.geometry("350x200")  # ancho x alto en píxeles

# 2) Crear una etiqueta (texto) y mostrarla con pack()
etiqueta = tk.Label(ventana, text="¡Hola, mundo!", font=("Arial", 18))
etiqueta.pack(pady=20)  # pady = espacio vertical alrededor


# 3) Función que se ejecuta cuando se presiona el botón
def cambiar_texto():
    etiqueta.config(text="¡Presionaste el botón!")


# 4) Crear el botón y conectarlo con la función usando command=
boton = tk.Button(ventana, text="Presióname", command=cambiar_texto)
boton.pack()

# 5) mainloop() mantiene la ventana abierta y escuchando eventos
ventana.mainloop()
