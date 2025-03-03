from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_greet():
    response = client.get("/greet/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}
