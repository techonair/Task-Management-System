# Task Management System

A FastAPI-based application to manage tasks with PostgreSQL, SQLAlchemy, and Alembic.

## Features

- Create, update, delete, and list tasks
- Task status: pending, in-progress, completed
- Pagination support
- Health check endpoint
- PostgreSQL with SQLAlchemy ORM
- Alembic for migrations

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL

### Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run Alembic migrations:

```bash
alembic upgrade head
```

4. Start the app:

```bash
uvicorn app.main:app --reload
```

### Environment Variables

Configure your database URL in `app/database.py`:

```python
DATABASE_URL = "postgresql://DUMMY-USERNAME:DUMMY-PASSWORD@localhost:5432/task_db"
```

## API Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Postman Collection

Postman-Collection/Task-Manager-API.postman_collection.json