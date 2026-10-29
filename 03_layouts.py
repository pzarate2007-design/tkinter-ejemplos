"""
03_layouts.py
Los tres administradores de posición (geometry managers) de Tkinter:
pack(), grid() y place().
IMPORTANTE: dentro de un mismo contenedor NO se deben mezclar pack y grid.
Por eso cada ejemplo vive en su propio LabelFrame.
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Layouts: pack, grid y place")
ventana.geometry("420x520")

# ---------- pack(): apila widgets uno tras otro ----------
marco_pack = tk.LabelFrame(ventana, text="pack()")
marco_pack.pack(fill="x", padx=10, pady=5)
tk.Button(marco_pack, text="Arriba").pack(side="top", fill="x")
tk.Button(marco_pack, text="Izquierda").pack(side="left")
tk.Button(marco_pack, text="Derecha").pack(side="right")

# ---------- grid(): cuadrícula de filas y columnas ----------
marco_grid = tk.LabelFrame(ventana, text="grid()")
marco_grid.pack(fill="x", padx=10, pady=5)
tk.Label(marco_grid, text="Usuario:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
tk.Entry(marco_grid).grid(row=0, column=1, padx=5, pady=3)
tk.Label(marco_grid, text="Contraseña:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
tk.Entry(marco_grid, show="*").grid(row=1, column=1, padx=5, pady=3)
tk.Button(marco_grid, text="Entrar").grid(row=2, column=0, columnspan=2, pady=5)

# ---------- place(): coordenadas exactas (x, y) ----------
marco_place = tk.LabelFrame(ventana, text="place()", height=150)
marco_place.pack(fill="x", padx=10, pady=5)
marco_place.pack_propagate(False)  # evita que el marco se encoja
tk.Label(marco_place, text="Posición (20, 20)", bg="lightyellow").place(x=20, y=20)
tk.Label(marco_place, text="Posición (200, 70)", bg="lightblue").place(x=200, y=70)

# ---------- Frame con proporciones usando grid + weight ----------
marco_resp = tk.LabelFrame(ventana, text="grid() adaptable (cambia el tamaño de la ventana)")
marco_resp.pack(fill="both", expand=True, padx=10, pady=5)
marco_resp.columnconfigure(0, weight=1)
marco_resp.columnconfigure(1, weight=1)
marco_resp.rowconfigure(0, weight=1)
tk.Button(marco_resp, text="Izquierda").grid(row=0, column=0, sticky="nsew")
tk.Button(marco_resp, text="Derecha").grid(row=0, column=1, sticky="nsew")

ventana.mainloop()
