# Gestor de Tareas (CLI)

Proyecto CLI sencillo para gestionar tareas desarrollado en Python.

## Descripción

Este repositorio contiene una aplicación de línea de comandos para crear, listar y administrar tareas.
El código fuente está en el paquete `src` y organizado en módulos `core`, `models` y `utils`.

## Requisitos

- Python 3.8+

Opcionalmente, crea un entorno virtual antes de instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
```

Si en el futuro hay dependencias, agrégalas a un `requirements.txt` e instala con:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

Desde la raíz del proyecto ejecuta:

```bash
python -m src.main
```

ó

```bash
python src/main.py
```

## Estructura del proyecto

- `src/`: código fuente
	- `core/`: lógica de la aplicación
	- `models/`: modelos de datos
	- `utils/`: utilidades y formateo

## Git

El repositorio ya está inicializado y vinculado a `origin` en GitHub.

Recomendaciones:

- Añade un archivo `.gitignore` para ignorar entornos virtuales y archivos temporales.
- Considera añadir un `LICENSE` si quieres un permiso explícito.

## Contribuciones

Si quieres colaborar, crea un fork, abre una rama, añade cambios y envía un pull request.

## Licencia

Sin licencia especificada — agrega un `LICENSE` si deseas definirla.
