#EJERCICIO 10 - Gestor de Tareas de Proyecto
#Crea un programa en Python que gestione una lista de tareas de proyecto. Los usuarios pueden agregar nuevas tareas, marcar tareas como completadas y ver el progreso del proyecto

#TIPO de dato que se quiere almacenar--> Información sobre tareas de proyecto. Generalmente, incluye el nombre o descripción(cadena de texto-str) y su estado de estar completa(booleano-bool)
#ESTRUCTURA de dato adecuada --> Para gestionar una lista de tareas de proyecto, la estructura adecuada es una lista de diccionarios.
#Cada diccionario contendrá la información de una tarea, incluyendo su nombre y en qué estado se encuentra para llegar a estar cmpleto.
#¿Cuánto OCUPA nuestra solución en espacio por usuario? dependerá de la cantidad de tareas que el usuario agregue al proyecto y de la cantidad de información asociada a cada tarea.
 #En este caso, cada tarea se representa como un diccionario, lo que implica un ligero aumento en el consumo de memoria en comparación con una lista simple.

class GestorTareasProyecto:
    def __init__(self):
       self.tareas = []

    def agregar_tarea(self, nombre_tarea):
       tarea = {"nombre": nombre_tarea, "completada": False}
    self.tareas.append(tarea)

    def marcar_completada(self, indice):
       if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
       else:
        print("Índice de tarea fuera de rango.")

    def ver_progreso(self):
       if len(self.tareas) == 0:
            print("El proyecto no tiene tareas.")
       else:
            tareas_completadas = sum(1 for tarea in self.tareas if tarea["completada"])
            total_tareas = len(self.tareas)
            progreso = (tareas_completadas / total_tareas) * 100
            print(f"Progreso del proyecto: {progreso:.2f}%")

#Ejemplo:
# Crear una instancia de la clase GestorTareasProyecto
gestor_proyecto = GestorTareasProyecto()
# Agregar tareas al proyecto
gestor_proyecto.agregar_tarea("Tarea 1")
gestor_proyecto.agregar_tarea("Tarea 2")
gestor_proyecto.agregar_tarea("Tarea 3")

# Marcar una tarea como completada
gestor_proyecto.marcar_completada(0)
# Ver el progreso del proyecto
gestor_proyecto.ver_progreso()
#Los métodos agregar_tarea agregarán nuevas tareas, marcar_completada permitirá marcar una tarea como completada (a través de su índice), y ver_progreso, calculará y mostrará el progreso del proyecto en términos de tareas completadas.
