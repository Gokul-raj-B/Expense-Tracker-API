# Expense Tracker API

A REST API built using FastAPI and PostgreSQL to manage personal expenses securely with JWT authentication. The application supports user registration, login, expense CRUD operations, and user-specific expense tracking.

## Features

* User registration with hashed passwords
* User login with JWT access tokens
* Password verification using Passlib and bcrypt
* Secure Bearer token authentication
* Create, read, update, and delete expenses
* User-specific expense access
* Calculate total expenses for the authenticated user
* PostgreSQL database integration
* SQLAlchemy ORM for database operations
* Environment variable management using `.env`
* Interactive API documentation using Swagger UI

## Technologies Used

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* PyJWT
* Passlib
* bcrypt
* Uvicorn
* python-dotenv
* Pydantic
* uv

## Project Structure

Expense_tracker_Api/
│
├── routers/
│   ├── users.py
│   └── expenses.py
│
├── main.py
├── auth.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .env
├── .gitignore
└── README.md

## Database Setup

This project uses PostgreSQL to store user accounts and expense records.

### 1. Create the Database

Open PostgreSQL using pgAdmin or `psql` and execute:

CREATE DATABASE expense_tracker_db;

Connect to the `expense_tracker_db` database before creating the tables.

**Note:** If you already created a database for this project, use that existing database instead of creating another one.

### 2. Create the Users Table

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);

### 3. Create the Expenses Table

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0),
    category VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    user_id INTEGER NOT NULL
        REFERENCES users(id) ON DELETE CASCADE
);

The `user_id` column links each expense to its owner. The foreign key also allows a user's associated expenses to be deleted automatically when that user is deleted.

## Setup Instructions

### 1. Clone the Repository

Replace the example URL with your actual GitHub repository URL.

git clone YOUR_GITHUB_REPOSITORY_URL


### 2. Create and Activate a Virtual Environment (Optional)

If you use Python's built-in virtual environment:

python -m venv .venv


Windows PowerShell:

.\.venv\Scripts\Activate.ps1


### 3. Install Dependencies

Using `pip`:

pip install -r requirements.txt

Alternatively, if you are using `uv` and have the project lock file:

uv sync

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/expense_tracker_db
SECRET_KEY=YOUR_SECRET_KEY
ALGORITHM=HS256


Replace `YOUR_PASSWORD` with your PostgreSQL password and `YOUR_SECRET_KEY` with a secure secret key. Ensure that the database name matches your actual PostgreSQL database.

**Security:** Never commit your `.env` file or real database credentials to GitHub. Make sure `.env` is included in `.gitignore`.

### 5. Run the Application

Using `uv`:


uv run uvicorn main:app --reload

Or, if dependencies are installed in your active virtual environment:


uvicorn main:app --reload

### 6. Open Swagger UI

Visit:

http://127.0.0.1:8000/docs

Use Swagger UI to register, log in, authorize using the JWT access token, and test the protected expense endpoints.

## API Endpoints

| Method | Endpoint                 | Purpose                                           |
| ------ | ------------------------ | ------------------------------------------------- |
| POST   | `/users/register`        | Register a new user                               |
| POST   | `/users/login`           | Log in and receive a JWT token                    |
| POST   | `/expenses/`             | Create an expense                                 |
| GET    | `/expenses/`             | List the authenticated user's expenses            |
| GET    | `/expenses/total`        | Calculate the authenticated user's total expenses |
| PUT    | `/expenses/{expense_id}` | Update an expense owned by the user               |
| DELETE | `/expenses/{expense_id}` | Delete an expense owned by the user               |

## Authentication

The application uses JSON Web Tokens (JWT) to authenticate users.

1. Register a new account using `/users/register`.
2. Log in using `/users/login`.
3. Copy the returned access token.
4. Click **Authorize** in Swagger UI and enter the token using the Bearer authentication option.
5. Access the protected expense endpoints.

Passwords are stored as hashes rather than plain text. Expense operations are restricted to the authenticated user, preventing users from accessing or modifying other users' expense records through these endpoints.

The `auth.py` module contains reusable authentication functions for password hashing, password verification, JWT creation, and current-user validation.

## Future Improvements

* Daily and monthly expense summaries
* Expense category analytics
* Date-based expense filtering
* Pagination for expense records
* Automated testing
* Expense reports and visualizations

## Author

**Gokulraj B**
