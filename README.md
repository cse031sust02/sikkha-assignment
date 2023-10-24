# Assignment for a Company

## Description

This is the the backend system for an online learning platform.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)

## Installation

> Install docker and docker compose on your PC if you do not have already

This project is dockerized. You can run the application by simply using docker compose

```
docker-compose up
```

## API Endpoints

### Courses API

- `GET /courses`: Retrieve a list of available courses.
- `GET /courses/<id>`: Retrieve a specific course by its ID.
- `POST /courses`: Create a new course.

I have also added swagger for this project. You can check the swagger doc here localhost:8000/api/docs

### Enrollments API

- `POST /enrollments`: Allow students to enroll in a course.

[Provide examples for each API endpoint, including sample request and response data.]

## Dependencies

[Include a list of dependencies required to run the application, such as Django, Django REST framework, and any other third-party libraries.]

## Environment Variables

[Specify any required environment variables, such as database credentials, API keys, or other sensitive information. Provide instructions on how to set these variables.]

## Contributing

[Include guidelines for contributing to the project, if applicable.]

## License

[Specify the project's license information.]

## Contact

[Provide your contact information if users have any questions or need assistance.]

