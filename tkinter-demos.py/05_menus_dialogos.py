"""
05_menus_dialogos.py
Barra de menú, cuadros de diálogo (messagebox) y selector de archivos (filedialog).
Es un mini editor de texto: abrir, guardar y salir.
"""
import tkinter as tk
from tkinter import messagebox, filedialog

ventana = tk.Tk()
ventana.title("Mini editor de texto")
ventana.geometry("550x400")

# --- Text con barra de desplazamiento (Scrollbar) ---
marco = tk.Frame(ventana)
marco.pack(fill="both", expand=True)
scroll = tk.Scrollbar(marco)
scroll.pack(side="right", fill="y")
texto = tk.Text(marco, yscrollcommand=scroll.set, wrap="word")
texto.pack(fill="both", expand=True)
scroll.config(command=texto.yview)


def nuevo():
    if messagebox.askyesno("Nuevo", "¿Borrar todo el contenido actual?"):
        texto.delete("1.0", tk.END)  # "1.0" = línea 1, carácter 0


def abrir():
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")]
    )
    if ruta:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                texto.delete("1.0", tk.END)
                texto.insert("1.0", f.read())
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{error}")


def guardar():
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Guardado", "Archivo guardado correctamente.")


def acerca_de():
    messagebox.showinfo("Acerca de", "Mini editor hecho con Tkinter.")


def salir():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()


# --- Barra de menú ---
barra = tk.Menu(ventana)
ventana.config(menu=barra)

menu_archivo = tk.Menu(barra, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Abrir...", command=abrir)
menu_archivo.add_command(label="Guardar como...", command=guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(barra, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra.add_cascade(label="Ayuda", menu=menu_ayuda)

# Qué hacer cuando se presiona la "X" de la ventana
ventana.protocol("WM_DELETE_WINDOW", salir)

ventana.mainloop()
