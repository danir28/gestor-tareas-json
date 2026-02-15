from .core.logic import agregar_tarea, listar_tareas, eliminar_tarea, completar_tarea
from .utils.formato import mostrar_tareas
from .utils.persistencia import cargar_tareas, guardar_tareas

RUTA = 'tareas.json'

tareas = cargar_tareas(RUTA)

while True:
    print()
    print('1. Agregar tarea')
    print('2. Listar tareas')
    print('3. Completar tarea')
    print('4. Eliminar tarea')
    print('5. Listar tareas pendientes')
    print('6. Listar tareas completas')
    print('7. Listar tareas por prioridad')
    print('8. Salir')
    print()
    
    opcion = input('Seleccione una opción: ')
    
    if opcion == '1':
        titulo = input('titulo: ')
        descripcion = input('descripcion (opcional): ')
        resultado = agregar_tarea(tareas, titulo, descripcion)
        if resultado == 0:
            guardar_tareas(tareas, RUTA)
            print('Tarea agregada exitosamente.')
        else:
            print('Error al agregar tarea. El título no puede estar vacío.')
    elif opcion == '2':
        tareas_para_mostrar = listar_tareas(tareas)
        mostrar_tareas(tareas_para_mostrar)
    elif opcion == '3':
        try:
            indice = int(input('Ingrese el número de la tarea a completar: ')) - 1
            resultado = completar_tarea(tareas, indice)
            if resultado == 0:
                guardar_tareas(tareas, RUTA)
                print('Tarea completada exitosamente.')
            else:
                print('Error al completar tarea. Índice inválido.')
        except ValueError:
            print('Error: esa tarea no existe')
    elif opcion == '4':
        try:
            indice = int(input('Ingrese el número de la tarea a eliminar: ')) - 1
            resultado = eliminar_tarea(tareas, indice)
            if resultado == 0:
                guardar_tareas(tareas, RUTA)
                print('Tarea eliminada exitosamente.')
            else:
                print('Error al eliminar tarea. Índice inválido.')
        except ValueError:
            print('Error: esa tarea no existe')
    elif opcion == '5':
        tareas_para_mostrar = listar_tareas(tareas, estado='pendiente')
        mostrar_tareas(tareas_para_mostrar)
    elif opcion == '6':
        tareas_para_mostrar = listar_tareas(tareas, estado='completo')
        mostrar_tareas(tareas_para_mostrar)
    elif opcion == '7':
        prioridad = input('Ingrese la prioridad a filtrar (baja, media, alta): ')
        tareas_para_mostrar = listar_tareas(tareas, prioridad=prioridad)
        mostrar_tareas(tareas_para_mostrar)
    elif opcion == '8':
        print('Saliendo del programa.')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 5.')