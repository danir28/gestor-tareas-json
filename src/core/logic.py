from ..models.tarea import Tarea

OK = 0
ERROR = 1

def agregar_tarea(tareas: list, titulo: str, descripcion: str = ""):
    if not titulo or not titulo.strip():
        return ERROR
    tarea = Tarea(titulo, descripcion)
    tareas.append(tarea)
    return OK

def listar_tareas(tareas: list):
    return tareas

def completar_tarea(tareas: list, indice: int):
    if indice < 0 or indice >= len(tareas):
        return ERROR
    tareas[indice].completada = True
    return OK

def eliminar_tarea(tareas: list, indice: int):
    if indice < 0 or indice >= len(tareas):
        return ERROR
    del tareas[indice]
    return OK
