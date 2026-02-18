# Todo API

A RESTful Todo API built with FastAPI and SQLAlchemy.

This project implements a clean, layered backend architecture with standardized API responses, validation, pagination, and statistics endpoints.

------------------------------------------------------------

TECH STACK

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic (v2)
- Uvicorn

------------------------------------------------------------

PROJECT STRUCTURE

app/
 ├── api/
 │    ├── deps.py
 │    └── routes/
 │         └── todos.py
 ├── core/
 │    └── config.py
 ├── db/
 │    ├── base.py
 │    └── session.py
 ├── models/
 │    └── todo.py
 ├── schemas/
 │    ├── todo.py
 │    └── response.py
 ├── services/
 │    └── todo_service.py
 └── main.py

The project follows a layered architecture:

- Models: Database structure
- Schemas: Request/response validation
- Services: Business logic
- Routes: HTTP layer
- Core/DB: Configuration and database setup

------------------------------------------------------------

SETUP INSTRUCTIONS

Clone the repository:

git clone https://github.com/ojifadslnmk/todo-api.git
cd todo-api

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive documentation (Swagger UI):

http://127.0.0.1:8000/docs

------------------------------------------------------------

API ENDPOINTS

Todos:

GET     /api/todos
GET     /api/todos/{id}
POST    /api/todos
PUT     /api/todos/{id}
DELETE  /api/todos/{id}
PATCH   /api/todos/{id}/toggle
GET     /api/todos/stats

Pagination is supported via query parameters:
- skip
- limit

Example:
GET /api/todos?skip=0&limit=10

------------------------------------------------------------

RESPONSE FORMAT

All successful responses follow this structure:

{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}

Error responses follow this structure:

{
  "success": false,
  "error": "Error message",
  "errors": {
    "field": ["Validation error"]
  }
}

------------------------------------------------------------

FEATURES IMPLEMENTED

- Full CRUD operations
- Toggle completion endpoint
- Pagination support
- Todo statistics endpoint
- Standardized success responses
- Centralized error handling
- Input validation with Pydantic
- Environment-based configuration
- Clean layered architecture
- Proper HTTP status codes

------------------------------------------------------------

DESIGN DECISIONS

- Layered architecture to separate concerns.
- Centralized error handling for consistent API responses.
- SQLite chosen for simplicity and ease of setup.
- Pagination implemented for scalability.
- Configuration managed via environment variables.

------------------------------------------------------------

FUTURE IMPROVEMENTS

- JWT authentication
- Role-based access control
- Database migrations (Alembic)
- Automated tests
- Docker support
- Soft deletes
- Filtering by status

------------------------------------------------------------

NOTES

This project was developed as part of a backend assignment and focuses on clean architecture, best practices, and maintainable code structure.
