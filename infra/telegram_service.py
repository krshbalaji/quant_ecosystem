# infra/telegram_service.py

import requests
import json
import os

# Load secrets safely
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, "infra", "secrets.json")

with open(SECRETS_FILE, "r") as f:
    secrets = json.load(f)

TOKEN = secrets["TELEGRAM_TOKEN"]
CHAT_ID = secrets["TELEGRAM_CHAT_ID"]

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"


# SEND MESSAGE
def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        requests.post(url, json=payload, timeout=10)
        print("Telegram message sent")

    except Exception as e:
        print("Telegram send error:", e)


# SEND MENU
def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            [{"text": "STATUS"}, {"text": "PERFORMANCE"}],
            [{"text": "POSITIONS"}, {"text": "MODE"}],
            [{"text": "START LIVE"}, {"text": "STOP LIVE"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }

    payload = {
        "chat_id": CHAT_ID,
        "text": "Institutional Control Panel",
        "reply_markup": keyboard
    }

    try:
        requests.post(url, json=payload, timeout=10)
        print("Telegram menu sent")

    except Exception as e:
        print("Telegram menu error:", e)


# RECEIVE UPDATES
def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {
        "timeout": 10
    }

    if offset:
        params["offset"] = offset

    try:

        response = requests.get(url, params=params, timeout=15)

        return response.json()

    except Exception as e:

        print("Telegram polling error:", e)

        return None
# COMPATIBILITY WRAPPER
def send_alert(text):
    send_message(text)
