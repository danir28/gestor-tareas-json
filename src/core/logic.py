from ..models.tarea import Tarea

OK = 0
ERROR = 1

def agregar_tarea(tareas: list, titulo: str, descripcion: str = "", prioridad = 'media'):
    if not titulo or not titulo.strip():
        return ERROR
    tarea = Tarea(titulo, descripcion, prioridad)
    tareas.append(tarea)
    return OK

def listar_tareas(tareas, estado = None, prioridad = None, ordenar_por = None):
    resultado = tareas
    
    if estado == 'pendiente':
        resultado = [t for t in resultado if not t.completada]
    if estado == 'completo':
        resultado = [t for t in resultado if t.completada]
    if prioridad:
        resultado = [t for t in resultado if t.prioridad == prioridad]
    if ordenar_por == 'fecha':
        resultado = sorted(resultado, key=lambda t: t.fecha_creacion)
    if ordenar_por == 'prioridad':
        orden_prioridad = {'baja': 1, 'media': 2, 'alta': 3}
        resultado = sorted(resultado, key=lambda t: orden_prioridad.get(t.prioridad, 0), reverse=True)
        
    return resultado

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
