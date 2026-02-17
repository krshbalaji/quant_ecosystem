import requests
from infra.secrets import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    requests.post(url, json=payload)


# REQUIRED BY telegram_listener
def send_alert(text):

    send_message(f"ALERT: {text}")


def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            ["STATUS", "PORTFOLIO"],
            ["START LIVE", "STOP LIVE"],
            ["START PAPER", "STOP PAPER"],
            ["EVOLVE", "RECOVERY MODE"],
            ["EMERGENCY STOP"]
        ],
        "resize_keyboard": True,
        "persistent": True
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

    r = requests.get(url, params=params)

    return r.json()
