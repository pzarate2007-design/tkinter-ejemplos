# 🖼️ Tkinter Demos: aprende interfaces gráficas con Python

Colección de **8 programas de ejemplo en Python** que muestran, paso a paso, las funcionalidades principales de **Tkinter**, la librería estándar de Python para crear ventanas y aplicaciones de escritorio.

Cada archivo es independiente, está comentado línea por línea y va aumentando en dificultad: empieza con una ventana vacía y termina con una calculadora funcional.

---

## 📋 Requisitos

- **Python 3.8 o superior** ([descargar](https://www.python.org/downloads/)).
- **Tkinter** viene incluido con Python en Windows y macOS. No hay que instalar nada con `pip`.
  - En Linux (Ubuntu/Debian) puede hacer falta: `sudo apt install python3-tk`

Comprueba que funciona con:

```bash
python -m tkinter
```

Si se abre una ventanita de prueba, todo está listo.

## ▶️ Cómo ejecutar los ejemplos

1. Clona o descarga este repositorio.
2. Abre la carpeta en tu terminal o en Visual Studio Code.
3. Ejecuta cualquier archivo, por ejemplo:

```bash
python 01_hola_mundo.py
```

> En Windows, si `python` no funciona, prueba con `py 01_hola_mundo.py`. En macOS/Linux usa `python3`.

---

## 📁 Estructura del repositorio

```
tkinter-demos/
├── 01_hola_mundo.py
├── 02_widgets_basicos.py
├── 03_layouts.py
├── 04_eventos.py
├── 05_menus_dialogos.py
├── 06_canvas_dibujo.py
├── 07_lista_tareas.py
├── 08_calculadora.py
├── .gitignore
├── LICENSE
└── README.md
```

## 📚 Resumen rápido

| Archivo | Tema | Nivel |
|---|---|---|
| `01_hola_mundo.py` | Ventana, Label, Button | ⭐ |
| `02_widgets_basicos.py` | Entry, Checkbutton, Radiobutton, Combobox, Listbox, Scale, Spinbox | ⭐ |
| `03_layouts.py` | `pack()`, `grid()`, `place()` | ⭐⭐ |
| `04_eventos.py` | `bind()`, teclado, mouse, `after()` | ⭐⭐ |
| `05_menus_dialogos.py` | Menu, messagebox, filedialog, Text, Scrollbar | ⭐⭐ |
| `06_canvas_dibujo.py` | Canvas, figuras, animación con teclado | ⭐⭐⭐ |
| `07_lista_tareas.py` | App de tareas (Listbox + Entry) | ⭐⭐⭐ |
| `08_calculadora.py` | Calculadora completa | ⭐⭐⭐ |

---

## 🔎 Detalle de cada archivo

### `01_hola_mundo.py`
**Qué hace:** abre una ventana con un texto y un botón. Al presionar el botón, el texto cambia.

**Conceptos que enseña:**
- `tk.Tk()`: crea la ventana principal.
- `title()` y `geometry()`: ponen el título y el tamaño.
- `tk.Label`: muestra texto.
- `tk.Button` con `command=`: ejecuta una función al hacer clic.
- `pack()`: coloca el widget en la ventana.
- `mainloop()`: mantiene la ventana abierta esperando acciones del usuario.

---

### `02_widgets_basicos.py`
**Qué hace:** formulario con los widgets más usados. Al presionar **"Mostrar resumen"** se despliega en pantalla lo que el usuario eligió.

**Widgets incluidos:**
- `Entry`: caja de texto de una línea.
- `Checkbutton`: casilla que se marca/desmarca.
- `Radiobutton`: elegir una sola opción entre varias.
- `ttk.Combobox`: lista desplegable.
- `Listbox`: lista de elementos seleccionables.
- `Scale`: barra deslizante.
- `Spinbox`: número con flechas arriba/abajo.

**Concepto clave:** las **variables de Tkinter** (`StringVar`, `BooleanVar`) que guardan el valor de un widget y se actualizan automáticamente.

---

### `03_layouts.py`
**Qué hace:** muestra las tres formas de acomodar widgets dentro de una ventana, cada una en su propio recuadro.

- `pack()`: apila widgets (arriba, abajo, izquierda, derecha).
- `grid()`: los acomoda en filas y columnas, como una tabla (ideal para formularios).
- `place()`: posiciona con coordenadas exactas `x, y`.
- Ejemplo extra de `grid` con `weight`, para que los botones se estiren al cambiar el tamaño de la ventana.

**Regla importante:** dentro de un mismo contenedor **no se mezclan** `pack` y `grid`.

---

### `04_eventos.py`
**Qué hace:** una zona gris que reacciona al mouse y al teclado, y un reloj que cuenta segundos.

**Conceptos que enseña:**
- `bind()`: asocia un evento con una función.
- Eventos de mouse: clic izquierdo (`<Button-1>`), derecho (`<Button-3>`), doble clic, entrar y salir de un widget.
- Eventos de teclado: `<Key>`.
- El objeto `evento` y sus datos (`evento.x`, `evento.y`, `evento.keysym`).
- `after()`: ejecuta una función cada cierto tiempo sin congelar la ventana.

---

### `05_menus_dialogos.py`
**Qué hace:** un mini editor de texto con barra de menú para crear, abrir y guardar archivos `.txt`.

**Conceptos que enseña:**
- `Menu` con `add_command`, `add_cascade` y `add_separator`.
- `messagebox`: ventanas emergentes (`showinfo`, `showwarning`, `showerror`, `askyesno`, `askokcancel`).
- `filedialog`: abrir el explorador de archivos para elegir dónde abrir o guardar.
- `Text` + `Scrollbar`: área de texto con barra de desplazamiento.
- `protocol("WM_DELETE_WINDOW", ...)`: controlar qué pasa al presionar la "X".
- Manejo básico de errores con `try/except`.

---

### `06_canvas_dibujo.py`
**Qué hace:** un lienzo donde se dibujan figuras, se mueve un círculo con las **flechas del teclado** y se puede **pintar con el mouse**.

**Conceptos que enseña:**
- `Canvas` y sus métodos `create_rectangle`, `create_oval`, `create_line`, `create_polygon`, `create_text`.
- `coords()` y `move()` para mover objetos.
- Límites para que el objeto no se salga del lienzo.
- Evento `<B1-Motion>` (mover el mouse con el botón presionado).
- `delete("all")` para limpiar.

---

### `07_lista_tareas.py`
**Qué hace:** aplicación para agregar, completar y eliminar tareas.

**Conceptos que enseña:**
- Combinar `Entry`, `Listbox`, `Scrollbar` y botones en una app real.
- `curselection()` para saber qué elemento está seleccionado.
- `itemconfig()` para cambiar el aspecto de un elemento.
- Validaciones con `messagebox.showwarning`.
- Atajo de teclado: `Enter` agrega la tarea.

---

### `08_calculadora.py`
**Qué hace:** calculadora con las cuatro operaciones básicas, punto decimal y botón de limpiar.

**Conceptos que enseña:**
- Crear botones dentro de un bucle `for` y colocarlos con `grid`.
- `lambda` para pasar argumentos a `command`.
- Evaluar expresiones con `eval()` de forma controlada: solo se aceptan números y operadores.
- Manejo de errores (por ejemplo, división entre cero muestra `Error`).

---

## 🧠 Glosario rápido

| Término | Significado |
|---|---|
| **Widget** | Cualquier componente de la interfaz: botón, texto, lista, etc. |
| **Ventana raíz** | La ventana principal creada con `tk.Tk()`. |
| **Frame** | Contenedor invisible para agrupar widgets. |
| **Evento** | Algo que hace el usuario: clic, tecla, mover el mouse. |
| **Callback** | Función que se ejecuta cuando ocurre un evento o se presiona un botón. |
| **Mainloop** | Ciclo que mantiene la ventana viva y atenta a eventos. |

## 📖 Recursos para seguir aprendiendo

- [Documentación oficial de tkinter](https://docs.python.org/es/3/library/tkinter.html)
- [Documentación de tkinter.ttk](https://docs.python.org/es/3/library/tkinter.ttk.html)

## 📄 Licencia

Distribuido bajo licencia MIT. Consulta el archivo `LICENSE`.
