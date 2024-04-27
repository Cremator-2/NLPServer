import requests
from core.config import settings

BASE_URL = settings.URL + "/similarity"

line1 = "Я хочу услышать больше о вашей организации"
line2 = "Расскажите подробнее о вашей компании"

methods = [
    "jaccard", "cosine", "levenshtein", "hamming", "sorensen",
    "overlap", "damerau_levenshtein", "jaro", "strcmp95",
    "needleman_wunsch", "gotoh", "smith_waterman"
]


def test_similarity(method, line1, line2):
    request_url = f"{BASE_URL}/"
    json_payload = {
        "method": method,
        "line1": line1,
        "line2": line2
    }
    response = requests.post(request_url, json=json_payload)
    print(f"Method: {method}")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Response: {response.json()}")
    else:
        print(f"Error: {response.json()}")
    print("-" * 50)


if __name__ == "__main__":
    for method in methods:
        test_similarity(method, line1, line2)
