# Gestor de Tareas (CLI)

Aplicación de línea de comandos desarrollada en Python para gestionar tareas con persistencia en archivo JSON.

Permite agregar, listar, completar y eliminar tareas manteniendo los datos guardados entre ejecuciones.

Proyecto creado con fines educativos y de portfolio, aplicando separación por capas y buenas prácticas de organización del código.

---

## Funcionalidades

- Agregar tareas
- Listar tareas
- Marcar tareas como completadas
- Eliminar tareas
- Guardado automático en `tareas.json`
- Arquitectura modular (core / models / utils)

---

## Tecnologías

- Python 3.8+
- CLI (terminal)
- JSON para persistencia de datos

---

## Estructura del proyecto

gestor_tareas/
src/
main.py # interfaz CLI
core/ # lógica de negocio
models/ # entidades del dominio
utils/ # formateo y persistencia

### Descripción de capas

- **models** → define la entidad `Tarea`
- **core** → reglas de negocio (agregar, completar, eliminar)
- **utils** → impresión y guardado/carga JSON
- **main** → interacción con el usuario

Separar responsabilidades facilita mantenimiento, testing y escalabilidad.

---

## Instalación

Opcionalmente crear entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
