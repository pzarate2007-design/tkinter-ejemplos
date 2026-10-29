"""
06_canvas_dibujo.py
Canvas: dibujar figuras y mover un objeto con las flechas del teclado.
"""
import tkinter as tk

ANCHO, ALTO = 500, 350
PASO = 10  # píxeles que se mueve el círculo por pulsación

ventana = tk.Tk()
ventana.title("Canvas: dibujo y movimiento")

lienzo = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="white")
lienzo.pack()

# --- Figuras estáticas ---
lienzo.create_rectangle(20, 20, 120, 80, fill="lightblue", outline="navy", width=2)
lienzo.create_line(150, 20, 300, 80, fill="red", width=3)
lienzo.create_polygon(350, 80, 400, 20, 450, 80, fill="orange", outline="black")
lienzo.create_text(250, 330, text="Usa las flechas del teclado", font=("Arial", 12))

# --- Círculo que se puede mover ---
circulo = lienzo.create_oval(225, 150, 275, 200, fill="green")


def mover(dx, dy):
    x1, y1, x2, y2 = lienzo.coords(circulo)
    # Evitar que salga del lienzo
    if x1 + dx < 0 or x2 + dx > ANCHO or y1 + dy < 0 or y2 + dy > ALTO:
        return
    lienzo.move(circulo, dx, dy)


ventana.bind("<Up>", lambda e: mover(0, -PASO))
ventana.bind("<Down>", lambda e: mover(0, PASO))
ventana.bind("<Left>", lambda e: mover(-PASO, 0))
ventana.bind("<Right>", lambda e: mover(PASO, 0))


# --- Dibujar con el mouse manteniendo el botón presionado ---
def dibujar(evento):
    lienzo.create_oval(
        evento.x - 2, evento.y - 2, evento.x + 2, evento.y + 2, fill="purple", outline=""
    )


lienzo.bind("<B1-Motion>", dibujar)

tk.Button(ventana, text="Limpiar dibujos", command=lambda: lienzo.delete("all")).pack(pady=5)

ventana.mainloop()
