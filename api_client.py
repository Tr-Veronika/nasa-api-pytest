import requests

from config import TIMEOUT


def get_json(url, params=None):
    response = requests.get(
        url,
        params=params,
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
