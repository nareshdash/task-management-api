# Task Management API

A production-style Task Management REST API built with Django REST Framework.

This project demonstrates backend development practices including JWT authentication, Role-Based Access Control (RBAC), PostgreSQL integration, Swagger documentation, filtering, search, pagination, automated testing, and clean API design.

---

# 🚀 Features

- Dockerized application for easy setup

## Authentication
- JWT Authentication using Simple JWT
- Secure API endpoints
- Token refresh support
- Password hashing using Django authentication system

## Role Based Access Control (RBAC)

### Admin
- View all tasks
- Manage all users' tasks
- Full access

### User
- Create tasks
- View own tasks
- Update own tasks
- Delete own tasks

## Task Management
- Create tasks
- Update tasks
- Delete tasks
- View task details
- Mark task as completed
- Toggle task completion status

## API Features
- RESTful API design
- PostgreSQL database integration
- Filtering
- Search
- Pagination
- Swagger API documentation
- ReDoc API documentation

---

# 🛠 Tech Stack

## Backend
- Python 3.10+
- Django
- Django REST Framework

## Database
- PostgreSQL

## DevOps
- Docker
- Docker Compose

## Authentication
- djangorestframework-simplejwt

## Documentation
- drf-yasg (Swagger UI)
- ReDoc

## Additional Packages
- django-filter
- python-dotenv

---

# 📂 Project Structure

task_api_project/

├── api/  
│   ├── models.py  
│   ├── serializers.py  
│   ├── views.py  
│   ├── permissions.py  
│   ├── urls.py  
│   └── tests/  
│       ├── test_auth.py  
│       ├── test_tasks.py  
│       └── test_permissions.py  
│  
├── core/  
│   ├── settings.py  
│   ├── urls.py  
│   ├── wsgi.py  
│   └── asgi.py  
│  
├── manage.py  
├── Dockerfile  
├── docker-compose.yml  
├── requirements.txt  
├── .env.example  
└── README.md  

---

# ⚙️ Installation & Setup (Local)

1. Clone Repository  
git clone https://github.com/nareshdash/task-management-api.git  
cd task-management-api  

2. Create Virtual Environment  

Linux / Mac:  
python3 -m venv venv  
source venv/bin/activate  

Windows:  
python -m venv venv  
venv\Scripts\activate  

3. Install Dependencies  
pip install -r requirements.txt  

4. Setup Environment Variables (.env)

SECRET_KEY=your_secret_key  
DEBUG=True  
DB_NAME=taskdb  
DB_USER=postgres  
DB_PASSWORD=postgres  
DB_HOST=localhost  
DB_PORT=5432  

5. Run Migrations  
python manage.py migrate  

6. Create Superuser  
python manage.py createsuperuser  

7. Run Server  
python manage.py runserver  

---

# 🐳 Docker Setup (Recommended)

This project is fully containerized using Docker and Docker Compose.

## Run with Docker

1. Build and start containers:  
docker compose up --build  

2. Apply migrations:  
docker compose exec web python manage.py migrate  

3. Create superuser:  
docker compose exec web python manage.py createsuperuser  

---

## Access Application

API Root:  
http://127.0.0.1:8000/api/

Swagger Docs:  
http://127.0.0.1:8000/swagger/

ReDoc:  
http://127.0.0.1:8000/redoc/

---

## Services

- web → Django application  
- db → PostgreSQL database  

---

## Important Notes

- PostgreSQL runs inside Docker container  
- Django connects using DB_HOST=db inside Docker  
- Do NOT use localhost inside Docker  

---

# 📌 API Endpoints

Base URL:  
http://127.0.0.1:8000/api/

---

## 🔐 Authentication

### Register  
POST /api/register/

Request:
{
  "username": "john",
  "password": "password123"
}

---

### Login  
POST /api/login/

Request:
{
  "username": "john",
  "password": "password123"
}

Response:
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}

---

### Refresh Token  
POST /api/refresh/

Request:
{
  "refresh": "your_refresh_token"
}

---

## 📋 Tasks

### List Tasks  
GET /api/tasks/

### Create Task  
POST /api/tasks/

Request:
{
  "title": "My Task",
  "description": "Task description",
  "is_completed": false
}

### Retrieve Task  
GET /api/tasks/{id}/

### Update Task  
PUT /api/tasks/{id}/

### Partial Update  
PATCH /api/tasks/{id}/

### Delete Task  
DELETE /api/tasks/{id}/

### Toggle Task Completion  
POST /api/tasks/{id}/toggle/

---

# 🔍 Filtering

GET /api/tasks/?is_completed=true  
GET /api/tasks/?is_completed=false  

---

# 🔎 Search

GET /api/tasks/?search=meeting  

---

# 📄 Pagination

GET /api/tasks/?page=2  

---

# 🔑 Authentication Usage

Authorization: Bearer <access_token>

---

# 🔐 Permission Logic

Admin:
- Can view all tasks  
- Can manage all tasks  

User:
- Can only access their own tasks  

---

# 🧪 Testing

python manage.py test  

---

# 🔒 Security Practices

- Environment-based secrets  
- JWT authentication  
- Role-based permissions  
- Password hashing  
- Protected endpoints  

---

# 📖 API Documentation

Swagger:  
http://127.0.0.1:8000/swagger/

ReDoc:  
http://127.0.0.1:8000/redoc/

---

# 📸 Screenshots

![Swagger Auth](screenshots/swagger-auth.png)  
![Swagger Tasks](screenshots/swagger-tasks.png)  
![Swagger Response](screenshots/swagger-response.png)  
![Django Admin](screenshots/admin.png)  

---

# 🚀 Future Improvements

- Production deployment setup  
- Advanced filtering (priority, due date)  
- Improved role management (admin dashboard)  
- API rate limiting  

---

# 👨‍💻 Author

Naresh Dash  
Backend Developer  
Python | Django | DRF | PostgreSQL