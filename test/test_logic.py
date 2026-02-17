from src.core.logic import agregar_tarea, listar_tareas, completar_tarea
from src.models.tarea import Tarea

def test_agregar_tarea_valida():
    tareas = []
    resultado = agregar_tarea(tareas, "Estudiar", "Python")
    
    assert resultado == 0
    assert len(tareas) == 1
    assert tareas[0].titulo == "Estudiar"
    assert tareas[0].descripcion == "Python"

def test_agregar_tarea_con_prioridad():
    tareas = []
    agregar_tarea(tareas, "Importante", "Algo", "alta")

    assert tareas[0].prioridad == "alta"

def test_agregar_tarea_titulo_vacio():
    tareas = []
    resultado = agregar_tarea(tareas, "", "Algo")
    
    assert resultado == 1
    assert len(tareas) == 0

def test_listar_tareas():
    tareas = [Tarea('Test')]
    resultado = completar_tarea(tareas, 0)
    
    assert resultado == 0
    assert tareas[0].completada is True

def test_listar_pendientes():
    t1 = Tarea('Uno')
    t2 = Tarea('Dos')
    t2.completada = True
    
    tareas = [t1, t2]
    
    pendientes = listar_tareas(tareas, estado='pendiente')
    
    assert len(pendientes) == 1
    assert pendientes[0].titulo == 'Uno'

def test_ordenar_por_prioridad():
    t1 = Tarea('A', prioridad='baja')
    t2 = Tarea('B', prioridad='alta')
    
    tareas = [t1, t2]
    
    ordenadas = listar_tareas(tareas, ordenar_por='prioridad')
    
    assert ordenadas[0].titulo == 'B'
    