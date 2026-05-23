# FastAPI + PostgreSQL REST API

A clean and scalable REST API built with FastAPI, PostgreSQL, and SQLAlchemy (Async ORM).

This project demonstrates a complete CRUD API with asynchronous database operations using SQLAlchemy and PostgreSQL.

---

# Features

- FastAPI framework
- PostgreSQL database
- Async SQLAlchemy ORM
- CRUD operations
- Pydantic schema validation
- Dependency Injection with FastAPI
- Automatic Swagger API docs
- Clean project structure

---

# Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- AsyncPG
- Pydantic
- Uvicorn

---

# Project Structure

```bash
project/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd project
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE fastapi_db;
```

---

# Configure Database

Update your `database.py` file:

```python
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/fastapi_db"
```

Replace:

- `postgres` → your PostgreSQL username
- `password` → your PostgreSQL password
- `fastapi_db` → your database name

---

# Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API docs.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/items/` | Create item |
| GET | `/items/` | Get all items |
| GET | `/items/{item_id}` | Get single item |
| PUT | `/items/{item_id}` | Update item |
| DELETE | `/items/{item_id}` | Delete item |

---

# Example Request

## Create Item

### Request

```http
POST /items/
Content-Type: application/json
```

```json
{
  "title": "Laptop",
  "description": "MacBook Pro"
}
```

### Response

```json
{
  "id": 1,
  "title": "Laptop",
  "description": "MacBook Pro"
}
```

---

# Example cURL Commands

## Create

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Phone",
  "description": "iPhone 15"
}'
```

## Get All

```bash
curl "http://127.0.0.1:8000/items/"
```

## Get One

```bash
curl "http://127.0.0.1:8000/items/1"
```

## Update

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Phone",
  "description": "Updated Description"
}'
```

## Delete

```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

---

# Requirements

`requirements.txt`:

```
txt
fastapi
uvicorn
sqlalchemy
asyncpg
psycopg2-binary
pydantic
```

---

# Future Improvements

- JWT Authentication
- Pagination
- Docker support
- Alembic migrations
- Environment variables with `.env`
- Testing with Pytest
- CI/CD pipeline

---

# License

This project is licensed under the MIT License.

---

# Author

Built with FastAPI, PostgreSQL, and SQLAlchemy.
