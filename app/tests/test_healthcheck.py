from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/healthcheck/ping")
    assert response.status_code == 200
    assert response.text == '"pong"'


def test_echo():
    data_items = [
        "Hello!",
        list("World!"),
        {"key": "value"}
    ]
    for item in data_items:
        response = client.post(f"/healthcheck/echo?request={item}")
        assert response.status_code == 200
        assert response.content.decode('utf-8') == f'"{item}"'
