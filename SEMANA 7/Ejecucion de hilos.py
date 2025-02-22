import threading
import time

# Función que simula un proceso ejecutado por un hilo
def tarea_proceso(nombre, delay):
    for paso in range(3):
        print(f'{nombre} ejecutando paso {paso}')
        time.sleep(delay)

# Creación y configuración de hilos
tarea_1 = threading.Thread(target=tarea_proceso, args=("Proceso A", 1.5))
tarea_2 = threading.Thread(target=tarea_proceso, args=("Proceso B", 1.0))
tarea_3 = threading.Thread(target=tarea_proceso, args=("Proceso C", 0.5))

tarea_1.start()
tarea_2.start()
tarea_3.start()

# Esperar a que los hilos terminen
tarea_1.join()
tarea_2.join()
tarea_3.join()

print('Finalización del programa: Todas las tareas han concluido.')