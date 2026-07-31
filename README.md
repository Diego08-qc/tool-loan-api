# ToolLoanAPI

## Descripción

ToolLoanAPI es una API REST desarrollada con **FastAPI** para la gestión de préstamo de herramientas. El proyecto permite administrar herramientas, prestatarios y préstamos, implementando operaciones CRUD sobre cada una de estas entidades.

Este proyecto fue desarrollado como parte de la materia de Desarrollo Backend, utilizando una arquitectura modular y buenas prácticas para la organización del código.

---

## Tecnologías utilizadas

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker
- Docker Compose
- Pydantic
- Python 3.13

---

## Estructura del proyecto

```
ToolLoanAPI/
│
├── alembic/
├── app/
│   ├── crud/
│   ├── db/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── .env
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Requisitos

Antes de ejecutar el proyecto es necesario tener instalado:

- Docker Desktop
- Docker Compose

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/tool-loan-api.git
cd tool-loan-api
```

---

### 2. Configurar variables de entorno

Crear un archivo **.env** tomando como base el archivo **.env.example**.

---

### 3. Construir y ejecutar el proyecto

```bash
docker compose up --build
```

---

## Migraciones

Para aplicar las migraciones de la base de datos:

```bash
docker compose exec api sh
```

Después ejecutar:

```bash
alembic upgrade head
```

---

## Documentación

Una vez iniciada la aplicación, la documentación interactiva estará disponible en:

```
http://localhost:8000/docs
```

---

## Funcionalidades

El proyecto incluye CRUD completo para las siguientes entidades:

- Tools
- Borrowers
- Loans

Cada entidad permite:

- Crear registros
- Consultar registros
- Actualizar registros
- Eliminar registros

---

## Autor

**Diego Quintero Calderón**

Desarrollo de Software
