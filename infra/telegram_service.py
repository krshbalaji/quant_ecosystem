import requests
import json
from infra.secrets import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    requests.post(url, json=payload)


def send_alert(text):

    send_message("🚨 " + text)


def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            ["START", "STOP"],
            ["STATUS", "MODE"],
            ["ENABLE LIVE", "DISABLE LIVE"],
            ["FORCE EXIT", "RESTART"]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "Quant Ecosystem Control Panel",
        "reply_markup": keyboard
    }

    requests.post(url, json=payload)


def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)

    return response.json()
