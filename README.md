# Basic CRUD with fastApi

CRUD básico usando fastapi y mongo fb

## Install the dependences
instalas las dependencias necesarias con el siguiente comando:

`pip install -r requirements.txt`

## Run the project
Para correr el pryecto usa el siguiente comando:

`uvicorn main:app --reload`

El pryecto se ejecutará en `localhost:8000/students`

## Project Structure

```
├── main.py
├── config
│   └── database.py
├── model
│   └── libros.py
├── routes
│   └── libros.py
└── schemas
    └── libros.py

```
* `main.py` archivo principal
* `routes/libros.py` archivo con las rutas de la api
* `model/libros.py` modelo de la base de datos
* `config/database.py` maneja la conección a la base de datos con mongodb
* `schemas/libros.py` modelo de pydantic