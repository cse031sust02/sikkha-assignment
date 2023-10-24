# Assignment for a Company

## Description

This is the the backend system for an online learning platform.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Installation

This project requires Docker and Docker Compose for easy setup and deployment.

Ensure you have Docker and Docker Compose installed on your system. If not, you can follow the official Docker documentation for installation instructions:

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

This project is dockerized. You can run the application using the following command:

```bash
docker-compose up
```

## API Endpoints

### Courses API

- `GET /courses`: Retrieve a list of available courses.
- `GET /courses/<id>`: Retrieve a specific course by its ID.
- `POST /courses`: Create a new course.


### Enrollments API

- `POST /enrollments`: Allow students to enroll in a course.

I have also added swagger for this project. You can check the API Docs here
- [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Dependencies

The project has the following dependencies:

- Django
- Django REST framework
- PostgreSQL
- Docker
- Docker Compose


## Contact
```
{
  "Name" : "Talha Ibne Imam",
  "Phone" : "01720205877",
  "Email" : "talha.imam.sust@gmail.com"
}
```
