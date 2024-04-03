import requests
from core.config import settings

BASE_URL = settings.URL + "/healthcheck"


def test_ping():
    response = requests.get(f"{BASE_URL}/ping")
    print("Ping Response:", response.json())


def test_echo():
    data = "Hello!"
    response = requests.post(f"{BASE_URL}/echo?request={data}")
    print("Echo Response:", response.json())


if __name__ == "__main__":
    test_ping()
    test_echo()
