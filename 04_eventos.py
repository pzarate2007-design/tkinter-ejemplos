"""
04_eventos.py
Eventos con bind(): clics, teclado, movimiento del mouse y temporizadores con after().
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Eventos")
ventana.geometry("450x350")

info = tk.Label(ventana, text="Haz clic, mueve el mouse o presiona teclas", font=("Arial", 11))
info.pack(pady=10)

zona = tk.Label(ventana, text="ZONA SENSIBLE", bg="lightgray", width=40, height=6)
zona.pack(pady=5)


# Cada función de evento recibe un parámetro "evento" con información
def clic_izquierdo(evento):
    info.config(text=f"Clic izquierdo en x={evento.x}, y={evento.y}")


def clic_derecho(evento):
    info.config(text=f"Clic derecho en x={evento.x}, y={evento.y}")


def doble_clic(evento):
    info.config(text="¡Doble clic!")


def entra_mouse(evento):
    zona.config(bg="lightgreen")


def sale_mouse(evento):
    zona.config(bg="lightgray")


def tecla(evento):
    info.config(text=f"Tecla presionada: {evento.keysym}")


zona.bind("<Button-1>", clic_izquierdo)
zona.bind("<Button-3>", clic_derecho)
zona.bind("<Double-Button-1>", doble_clic)
zona.bind("<Enter>", entra_mouse)
zona.bind("<Leave>", sale_mouse)
ventana.bind("<Key>", tecla)  # el teclado se enlaza a la ventana

# --- Temporizador con after(): ejecuta una función cada cierto tiempo ---
segundos = tk.IntVar(value=0)
reloj = tk.Label(ventana, text="Segundos abiertos: 0", font=("Arial", 12))
reloj.pack(pady=15)


def actualizar_reloj():
    segundos.set(segundos.get() + 1)
    reloj.config(text=f"Segundos abiertos: {segundos.get()}")
    ventana.after(1000, actualizar_reloj)  # se vuelve a llamar en 1000 ms


actualizar_reloj()

ventana.mainloop()
