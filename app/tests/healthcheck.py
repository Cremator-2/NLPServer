import requests

from core.config import settings

BASE_URL = settings.URL + "/healthcheck"


def test_ping():
    response = requests.get(f"{BASE_URL}/ping")
    print("Ping Status:", response.status_code)
    print("Ping Response:", response.text)


def test_echo(data):
    response = requests.post(f"{BASE_URL}/echo?request={data}")
    print("Echo Response:", response.json())


if __name__ == "__main__":
    test_ping()

    item = "Hello!"
    test_echo(item)

    item = {"key": "value"}
    test_echo(item)

