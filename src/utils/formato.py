def mostrar_tareas(tareas: list):
    if not tareas:
        print("No hay tareas para mostrar.")
    for idx, tarea  in enumerate(tareas):
        estado = 'completo' if tarea.completada else 'pendiente'
        print(f'{idx + 1}. {tarea.titulo} - Estado: {estado} - Prioridad: {tarea.prioridad} - Fecha de creacion: {tarea.fecha_creacion.strftime("%d-%m-%Y %H:%M:%S")} Descripcion: {tarea.descripcion}')
