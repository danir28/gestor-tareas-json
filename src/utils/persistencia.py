import json
import os
from ..models.tarea import Tarea

def guardar_tareas(tareas: list, ruta: str) -> None:
    data = []

    for tarea in tareas:
        data.append({
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'completada': tarea.completada
        })

    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def cargar_tareas(ruta: str) -> list:
    if not os.path.exists(ruta):
        return []
    
    with open(ruta, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tareas = []
    for item in data:
        tareas.append(
            Tarea(
                item['titulo'],
                item['descripcion'],
                item['completada']
            )
        )
    return tareas
