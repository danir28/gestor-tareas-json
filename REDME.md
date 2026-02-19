## Gestor de Tareas con Persistencia en JSON

Aplicación de consola desarrollada en Python que permite gestionar tareas con persistencia en archivo JSON.

Proyecto orientado a aplicar buenas prácticas de arquitectura, modularización, persistencia de datos y testing automatizado.

---

## Funcionalidades

-Agregar tareas
-Eliminar tareas
-Marcar tareas como completadas
-Listar tareas
-Filtrar por:
    -Estado (pendientes / completas)
    -Prioridad (baja / media / alta)
-Ordenar tareas por prioridad
-Persistencia automática en archivo JSON
-Tests automatizados con pytest

---

## Estructura del Proyecto

```bash
gestor_tareas_json/
│
├── src/
│   ├── core/
│   │   └── logic.py
│   ├── models/
│   │   └── tarea.py
│   ├── utils/
│   │   ├── persistencia.py
│   │   └── formato.py
│   └── main.py
│
├── test/
│   └── test_logic.py
│
├── tareas.json
└── README.md
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/danir28/gestor-tareas-json.git
cd gestor-tareas-json
```

Crear entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

instalar dependencias:

```bash
pip install pytest
```

---

## Ejecución

```bash
python3 -m src.main
```

---

## Tests

Ejecutar los tests con:

```bash
pytest
```

---

## Tecnologías utilizadas

-Python 3
-JSON
-pytest
-Git

---

## Objetivo del proyecto

Aplicar conceptos de:

-Programación orientada a objetos
-Modularización
-Persistencia de datos
-Testing automatizado
-Control de versiones