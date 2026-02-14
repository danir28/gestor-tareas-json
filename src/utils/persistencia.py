import json
import os
from ..models.tarea import Tarea
from datetime import datetime

def guardar_tareas(tareas: list, ruta: str) -> None:
    data = []

    for tarea in tareas:
        data.append({
            'id': tarea.id,
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'completada': tarea.completada,
            'prioridad': tarea.prioridad,
            'fecha_creacion': tarea.fecha_creacion.isoformat()
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
        tarea = Tarea(
                item['titulo'],
                item.get('descripcion', ''),
                item.get('prioridad', 'media')
            )
        
        tarea.id = item.get('id', tarea.id)
        tarea.completada = item.get('completada', False)
        fecha_creacion = item.get('fecha_creacion')
        if fecha_creacion:
            tarea.fecha_creacion = datetime.fromisoformat(item['fecha_creacion'])
        
        tareas.append(tarea)
        
    return tareas
