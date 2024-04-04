import requests

from core.config import settings
from models import example_dict

BASE_URL = settings.URL + "/healthcheck"


def test_ping():
    response = requests.get(f"{BASE_URL}/ping")
    print("Ping Response:", response.json())


def test_echo(data):
    response = requests.post(f"{BASE_URL}/echo?request={data}")
    print("Echo Response:", response.json())


if __name__ == "__main__":
    test_ping()

    item = "Hello!"
    test_echo(item)

    item = list("World!")
    test_echo(item)

    item = example_dict
    test_echo(item)

