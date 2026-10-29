"""
07_lista_tareas.py
App sencilla de lista de tareas: Entry + Listbox + Buttons + messagebox.
"""
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("380x420")

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(fill="x", padx=10, pady=10)
entrada.focus()  # el cursor empieza en la caja de texto

marco_lista = tk.Frame(ventana)
marco_lista.pack(fill="both", expand=True, padx=10)
scroll = tk.Scrollbar(marco_lista)
scroll.pack(side="right", fill="y")
lista = tk.Listbox(marco_lista, yscrollcommand=scroll.set, font=("Arial", 12))
lista.pack(fill="both", expand=True)
scroll.config(command=lista.yview)


def agregar(evento=None):
    tarea = entrada.get().strip()
    if not tarea:
        messagebox.showwarning("Atención", "Escribe una tarea primero.")
        return
    lista.insert(tk.END, tarea)
    entrada.delete(0, tk.END)


def eliminar():
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")
        return
    lista.delete(seleccion[0])


def completar():
    seleccion = lista.curselection()
    if seleccion:
        i = seleccion[0]
        lista.itemconfig(i, fg="gray")  # se ve "apagada"
        lista.selection_clear(0, tk.END)


entrada.bind("<Return>", agregar)  # Enter también agrega

botones = tk.Frame(ventana)
botones.pack(pady=10)
tk.Button(botones, text="Agregar", command=agregar).grid(row=0, column=0, padx=5)
tk.Button(botones, text="Completar", command=completar).grid(row=0, column=1, padx=5)
tk.Button(botones, text="Eliminar", command=eliminar).grid(row=0, column=2, padx=5)

ventana.mainloop()
