from datetime import datetime
import uuid

class Tarea:
    def __init__(self, titulo: str, descripcion: str = '', prioridad: str = 'media'):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now()
        
        if prioridad not in ['baja', 'media', 'alta']:
            prioridad = 'media'
        self.prioridad = prioridad
