import requests

from core.config import settings

BASE_URL = settings.URL + "/webhook"


def webhook(payload):
    requests.post(BASE_URL, json=payload)


if __name__ == "__main__":
    data = {
        'update_id': 798310433, 'message': {
            'message_id': 965,
            'from': {
                'id': 1761205412,
                'is_bot': False,
                'first_name': 'Илья',
                'username': 'Someone_Cremator',
                'language_code': 'ru'},
            'chat': {
                'id': 1761205412,
                'first_name': 'Илья',
                'username': 'Someone_Cremator',
                'type': 'private'
            },
            'date': 1712067878,
            'text': 'hi'
        }
    }
    webhook(data)

    data = "Hi!"
    webhook(data)
