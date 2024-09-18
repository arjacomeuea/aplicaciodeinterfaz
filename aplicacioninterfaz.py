import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)  # Agrega el dato al final de la lista
        entry_dato.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Borra todos los elementos de la lista

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")

# Etiqueta y campo de texto
label_dato = tk.Label(ventana, text="Ingrese un dato:")
label_dato.pack(pady=5)
entry_dato = tk.Entry(ventana, width=40)
entry_dato.pack(pady=5)

# Botón "Agregar"
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón "Limpiar"
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
