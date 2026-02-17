import requests
import json
from infra.secrets import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

LAST_UPDATE_ID = None


def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    r = requests.post(url, json=payload)

    print("Telegram message sent")

    return r.json()


def send_alert(text):

    return send_message(f"🚨 {text}")


def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            [{"text": "Status"}, {"text": "Equity"}],
            [{"text": "Positions"}, {"text": "Start LIVE"}],
            [{"text": "Stop LIVE"}, {"text": "Restart"}]
        ],
        "resize_keyboard": True
    }

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "Institutional Quant Ecosystem Ready",
        "reply_markup": keyboard
    }

    requests.post(url, json=payload)

    print("Telegram menu sent")


def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)

    return response.json()
