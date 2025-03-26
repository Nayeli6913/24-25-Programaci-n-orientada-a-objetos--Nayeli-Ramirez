import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

def agregar_con_enter(event):
    agregar_tarea()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada
tk.Label(ventana, text="Nueva Tarea:").pack(pady=5)
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_con_enter)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Iniciar el loop de la aplicación
ventana.mainloop()
