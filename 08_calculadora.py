"""
08_calculadora.py
Calculadora completa que junta lo aprendido: grid, Entry, Buttons y eventos.
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(False, False)

pantalla = tk.Entry(ventana, font=("Arial", 22), justify="right", width=16, bd=5)
pantalla.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

CARACTERES_VALIDOS = set("0123456789+-*/.() ")


def presionar(valor):
    pantalla.insert(tk.END, valor)


def limpiar():
    pantalla.delete(0, tk.END)


def calcular():
    expresion = pantalla.get()
    # Seguridad: solo permitimos números y operadores antes de usar eval()
    if not expresion or not set(expresion) <= CARACTERES_VALIDOS:
        return
    try:
        resultado = eval(expresion, {"__builtins__": {}}, {})
    except Exception:
        resultado = "Error"
    limpiar()
    presionar(str(resultado))


botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, fila, col in botones:
    if texto == "=":
        accion = calcular
    else:
        accion = lambda t=texto: presionar(t)  # t=texto "congela" el valor
    tk.Button(ventana, text=texto, font=("Arial", 16), width=4, height=2,
              command=accion).grid(row=fila, column=col, padx=3, pady=3)

tk.Button(ventana, text="C", font=("Arial", 16), bg="salmon", command=limpiar).grid(
    row=5, column=0, columnspan=4, sticky="nsew", padx=3, pady=3
)

ventana.mainloop()
