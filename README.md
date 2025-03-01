# FastAPI GitHub Actions Demo

This is a simple FastAPI application that demonstrates the use of GitHub Actions for CI/CD.

## Features

- FastAPI web application
- Poetry for dependency management
- Automated testing with pytest
- Code coverage reporting
- Code quality checks with black, isort, and flake8
- GitHub Actions workflows for continuous integration

## Setup

1. Clone the repository
2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Run the application:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

## Testing

Run tests with:
```bash
poetry run pytest
```

## Code Quality

Run code quality checks with:
```bash
poetry run black .
poetry run isort .
poetry run flake8 .
```

