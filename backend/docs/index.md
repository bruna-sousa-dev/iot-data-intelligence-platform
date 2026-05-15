![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC)
![Ruff](https://img.shields.io/badge/Ruff-Linting-46A146)
![Taskipy](https://img.shields.io/badge/Taskipy-Task%20Runner-orange)
![MkDocs](https://img.shields.io/badge/MkDocs-Documentation-526CFE)
![Status](https://img.shields.io/badge/Status-v0.1.0%20Backend%20Foundation-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)

# IoT Data Intelligence Platform API

The **IoT Data Intelligence Platform API** is the backend service of the IoT Data Intelligence Platform. It is built with **FastAPI** and provides the initial HTTP API foundation for future features such as authentication, IoT dataset upload, schema validation, dashboard metrics, and AI-assisted insights.

At the current stage, the backend is in version **`v0.1.0 - Backend foundation`**. This version establishes the initial application structure, centralized settings, router organization, a health check endpoint, development tasks, and automated testing for the initial API route.

---

## Current version

```text
v0.1.0 - Backend foundation
```

This version introduces the first stable backend foundation for the project. The goal is not yet to implement database, authentication, upload, dashboard, or AI features, but to provide a clean and scalable FastAPI structure for the next development stages.

---

## Implemented features

The current backend version includes:

- FastAPI application setup;
- centralized project settings;
- modular router structure;
- health check endpoint;
- response schema for the health check route;
- basic automated test for the health check endpoint;
- development task automation;
- MkDocs documentation structure.

---

## Project structure

The backend is organized as follows:

```text
backend/
├── app/
│   ├── configs/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health_routers.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── health_schemas.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── docs/
│   └── index.md
│
├── tests/
│   └── test_health.py
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── mkdocs.yml
├── pyproject.toml
├── requirements.txt
└── run.py
```

---

## Application architecture

The current backend follows a modular structure prepared for future growth.

### `app/main.py`

Main FastAPI application module.

This module is responsible for creating the FastAPI application instance and registering the available routers.

### `app/configs/settings.py`

Centralized application settings.

This module stores project-level configuration such as application metadata and versioning values. It is also the expected place for future environment-based settings, such as database URL, security keys, and external API configuration.

### `app/routers/health_routers.py`

Health check router.

This module defines the current health check endpoint used to verify whether the backend application is running correctly.

### `app/schemas/health_schemas.py`

Health check response schema.

This module defines the response structure returned by the health check endpoint.

### `tests/test_health.py`

Automated test for the health check endpoint.

This test verifies whether the endpoint responds successfully and returns the expected response payload for the current API version.

### `run.py`

Application entry point.

This file imports the FastAPI application from `app.main`. It can be used as an auxiliary entry point for running or referencing the application.

---

## API endpoint

### Health check

Verifies whether the backend service is running correctly.

```http
GET /api/health
```

#### Expected response

```json
{
  "status": "ok",
  "service": "IoT Data Intelligence Platform API",
  "version": "0.1.0"
}
```

#### Response fields

| Field     | Type     | Description                                                 |
|-----------|----------|-------------------------------------------------------------|
| `status`  | `string` | Indicates the current health status of the backend service. |
| `service` | `string` | Indicates the sevice name.                                  |
| `version` | `string` | Indicates the current backend version.                      |

---

## Local development

### Requirements

The backend requires:

- Python 3.12;
- FastAPI;
- Uvicorn;
- Pytest;
- Ruff;
- Taskipy;
- MkDocs.

The project configuration is defined in `pyproject.toml`.

---

## Running the API locally

From the `backend/` directory, run:

```bash
task run
```

The API will be available locally at:

```http
http://localhost:8000
```

FastAPI also provides automatic interactive documentation (Swagger):

```http
http://localhost:8000/docs
```

---

## Running tests

To execute the automated test suite, run:

```bash
task test
```

Current test coverage includes:

- successful health check response;
- HTTP status code validation;
- response payload validation;
- backend version validation.

The current test validates the health route using FastAPI's `TestClient`, without requiring the Uvicorn development server to be running.

---

## Running lint

To execute static code analysis, run:

```bash
task lint
```

The project uses Ruff for code quality checks.

---

## Environment configuration

The repository includes an `.env.example` file with the expected environment configuration pattern for the backend.

When environment variables are required, create a local `.env` file based on `.env.example`.

```bash
cp .env.example .env
```

The `.env` file must remain local and must not be committed to the repository.

---

## Development workflow

The current backend foundation supports a simple development workflow:

1. Run the API locally with `task run`.
2. Access the health endpoint at `/api/health`.
3. Validate the implementation with `task test`.
4. Check code quality with `task lint`.
5. Update the MkDocs documentation as new features are implemented.

---

## Version details

### v0.1.0 - Backend foundation

Implemented in this version:

- initial FastAPI application structure;
- centralized settings module;
- router package for API endpoints;
- schema package for response models;
- health check endpoint;
- automated test for the health check endpoint;
- initial MkDocs documentation structure.

Not included in this version:

- PostgreSQL database connection;
- SQLAlchemy models;
- Alembic migrations;
- user authentication;
- JWT security;
- IoT CSV upload;
- dataset validation;
- dashboard metrics;
- AI assistant integration;
- Docker environment;
- Nginx reverse proxy.

---

## Planned next steps

Upcoming backend milestones:

1. **Database integration**  
   Configure PostgreSQL connection and SQLAlchemy base setup.

2. **Migrations**  
   Add Alembic to control database schema evolution.

3. **User authentication**  
   Implement user registration, login, password hashing, and JWT-based protected routes.

4. **IoT dataset upload**  
   Add CSV upload support and dataset metadata storage.

5. **Dataset validation**  
   Validate required IoT columns and data types before persistence.

6. **Dashboard metrics API**  
   Provide analytical endpoints for frontend dashboard components.

7. **AI-assisted insights**  
   Add an assistant endpoint capable of interpreting uploaded IoT datasets.

---

## Documentation with MkDocs

This backend already includes a MkDocs structure:

```text
backend/
├── docs/
│   └── index.md
└── mkdocs.yml
```

This file can be used as a page inside the `docs/` directory, for example:

```text
backend/docs/api.md
```

Then, the page can be referenced in `mkdocs.yml`.

Example:

```yaml
site_name: IoT Data Intelligence Platform API

nav:
  - Home: index.md
  - Backend API: api.md
```

---

## Author

Developed by **Bruna Sousa**.

Electronic Engineer | IoT Developer | Web Developer | AI Developer

---

## License

This backend is part of the **IoT Data Intelligence Platform** project and is licensed under the MIT License.
