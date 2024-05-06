import requests

from core.config import settings

BASE_URL = settings.URL + "/processing/classifying"


def test_preprocessing(text):
    url = f"{BASE_URL}?text={text}"
    headers = {'Content-Type': 'text/plain'}

    response = requests.post(url, data="", headers=headers)

    print("Preprocessing Status Code:", response.status_code)
    print("Preprocessing Response:", response.text)


if __name__ == "__main__":
    text = """
    If you like original gut wrenching laughter you will like this movie. If you are young or old then you will love this movie, hell even my mom liked it.<br /><br />Great Camp!!!	
    """

    test_preprocessing(text)

