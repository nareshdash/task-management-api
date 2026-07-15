# Task Management API

A production-style Task Management REST API built with Django REST Framework.

This project demonstrates backend development practices including JWT authentication, Role-Based Access Control (RBAC), PostgreSQL integration, Swagger documentation, filtering, search, pagination, and clean API design.

---

# Features

## Authentication

- JWT Authentication using Simple JWT
- Secure API endpoints
- Token refresh support
- Password hashing using Django authentication system

---

## Role Based Access Control (RBAC)

### Admin

- View all tasks
- Manage all users' tasks
- Full access based on permissions

### User

- Create tasks
- View own tasks
- Update own tasks
- Delete own tasks

---

## Task Management

- Create tasks
- Update tasks
- Delete tasks
- View task details
- Mark task as completed
- Toggle task completion status

---

## API Features

- RESTful API design
- PostgreSQL database integration
- Filtering
- Search
- Pagination
- Swagger API documentation
- ReDoc API documentation

---

# Tech Stack

## Backend

- Python 3.10+
- Django
- Django REST Framework

## Database

- PostgreSQL

## Authentication

- djangorestframework-simplejwt

## Documentation

- drf-yasg Swagger UI
- ReDoc

## Additional Packages

- django-filter
- python-dotenv

---

# Project Structure

```text
task_api_project/

├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── admin.py
│
├── task_api_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-url>

cd task_api_project
```

---

# 2. Create Virtual Environment

## Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Database Setup

Create database:

```sql
CREATE DATABASE taskdb;
```

Create database user:

```sql
CREATE USER taskuser WITH PASSWORD 'your_password';
```

Grant permissions:

```sql
GRANT ALL PRIVILEGES ON DATABASE taskdb TO taskuser;
```

---

# Environment Configuration

Create `.env` file in the same directory where `manage.py` exists.

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=taskdb
DB_USER=taskuser
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

# Database Migration

Run migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# Create Admin User

Create Django admin user:

```bash
python manage.py createsuperuser
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# Run Development Server

```bash
python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

---

# API Documentation

## Swagger UI

Interactive API testing:

```text
http://127.0.0.1:8000/swagger/
```

---

## ReDoc

API reference documentation:

```text
http://127.0.0.1:8000/redoc/
```

---

# Authentication

## Get JWT Token

Endpoint:

```text
POST /api/token/
```

Request:

```json
{
    "username": "demo",
    "password": "demo@123"
}
```

Response:

```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

---

# Using JWT Token

For protected APIs add:

```text
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/token/ | Login and get token |
| POST | /api/token/refresh/ | Refresh token |


---

## Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks/ | List tasks |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/{id}/ | Task details |
| PUT | /api/tasks/{id}/ | Update task |
| DELETE | /api/tasks/{id}/ | Delete task |
| POST | /api/tasks/{id}/toggle/ | Toggle completion status |

---

# Filtering

Get completed tasks:

```text
GET /api/tasks/?is_completed=true
```

Get incomplete tasks:

```text
GET /api/tasks/?is_completed=false
```

---

# Search

Search tasks by title or description:

```text
GET /api/tasks/?search=meeting
```

---

# Pagination

Example:

```text
GET /api/tasks/?page=2
```

Response:

```json
{
    "count": 20,
    "next": "page_url",
    "previous": null,
    "results": []
}
```

---

# Permission Logic

## Admin

- Can view all tasks
- Can manage all tasks

## Normal User

- Can view only their own tasks
- Can create tasks
- Can update their own tasks
- Can delete their own tasks

Task ownership is automatically assigned during task creation.

---

# Security Practices

- Secrets stored using environment variables
- JWT authentication
- Role-based permissions
- Password hashing
- Protected API endpoints

---

# Screenshots

## Swagger Authentication

![Swagger Auth](screenshots/swagger-auth.png)

## Swagger Task APIs

![Swagger Tasks](screenshots/swagger-tasks.png)

## API Response

![Swagger Response](screenshots/swagger-response.png)

# Future Improvements

- Docker containerization
- CI/CD pipeline
- Redis caching
- Celery background jobs
- AWS deployment
- Automated API testing
- Rate limiting

---

# Author

## Naresh Dash

Backend Developer

Python | Django | Django REST Framework | PostgreSQL | REST APIs