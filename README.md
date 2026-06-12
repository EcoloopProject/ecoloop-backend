# EcoLoop Backend

Backend service for the EcoLoop platform.

This project provides the server-side APIs, business logic, authentication, and database operations required for the EcoLoop application.

## Features

* User authentication and authorization
* REST API endpoints
* Database integration
* Request validation
* Business logic services
* Environment-based configuration
* Scalable backend structure

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (development)
* HTML/CSS (admin templates)

## Project Structure

ecoloop-backend/

├── config/          Project configuration

├── core/            Main application modules

├── services/        Business logic and services

├── manage.py

├── requirements.txt

├── .env

└── db.sqlite3

## Installation

Clone the repository:

git clone https://github.com/EcoloopProject/ecoloop-backend.git

Move into the project directory:

cd ecoloop-backend

Install dependencies:

pip install -r requirements.txt

## Configuration

Create a `.env` file and configure the required environment variables.

Example:

DEBUG=True

SECRET_KEY=your_secret_key

## Database Setup

Run migrations:

python manage.py migrate

Create an admin account:

python manage.py createsuperuser

## Running the Server

Start the development server:

python manage.py runserver

The application will be available at:

http://127.0.0.1:8000/

## API Development

The backend exposes API endpoints that are consumed by the EcoLoop frontend. Additional endpoints can be added through the application modules inside the `core` and `services` directories.

## Current Status

The backend currently handles authentication, database operations, and API services required by the EcoLoop platform. Ongoing development focuses on feature enhancements, optimization, and deployment readiness.

## Author

Christeena Jestin
