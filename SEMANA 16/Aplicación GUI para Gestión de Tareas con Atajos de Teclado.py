import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task(event=None):
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

# Función para marcar tarea como completada
def complete_task(event=None):
    try:
        selected_task = listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task = listbox.get(task_index)
            listbox.delete(task_index)
            listbox.insert(task_index, f"{task} (Completada)")
            listbox.itemconfig(task_index, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

# Función para eliminar tarea
def delete_task(event=None):
    print("delete_task ejecutada")  # Depuración
    selected_task = listbox.curselection()  # Obtener la selección de tarea
    if selected_task:  # Si hay una tarea seleccionada
        task_index = selected_task[0]  # Obtener el índice de la tarea seleccionada
        print(f"Eliminando tarea en el índice {task_index}")  # Depuración
        listbox.delete(task_index)  # Eliminar la tarea en el índice seleccionado
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea primero")  # Si no hay tarea seleccionada

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Campo de entrada para agregar tarea
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para agregar tarea
add_button = tk.Button(root, text="Añadir tarea", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tarea como completada
complete_button = tk.Button(root, text="Marcar como completada", width=20, command=complete_task)
complete_button.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar tarea", width=20, command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Atajos de teclado
root.bind("<Return>", add_task)  # Tecla Enter para añadir tarea
root.bind("<c>", complete_task)  # Tecla "C" para completar tarea
root.bind("<BackSpace>", delete_task)  # Tecla Delete para eliminar tarea
root.bind("<d>", delete_task)  # Tecla "d" (minúscula) para eliminar tarea
root.bind("<Escape>", close_app)  # Tecla Escape para cerrar la aplicación

# Función para asegurar que el foco se ponga en el Listbox para usar atajos de teclado
def on_focus(event):
    listbox.focus_set()

# Asignar la acción de poner el foco en el Listbox cuando se haga clic
listbox.bind("<Button-1>", on_focus)

# Iniciar la interfaz
root.mainloop()
