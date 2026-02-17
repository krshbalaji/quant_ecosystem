# infra/telegram_service.py

import requests
import json
import os


# Load secrets
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRETS_PATH = os.path.join(BASE_DIR, "infra", "secrets.json")

with open(SECRETS_PATH, "r") as f:
    secrets = json.load(f)

TELEGRAM_TOKEN = secrets["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = secrets["TELEGRAM_CHAT_ID"]

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


# Send simple message
def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    try:
        requests.post(url, json=payload, timeout=10)
        print("Telegram message sent")

    except Exception as e:
        print("Telegram send error:", e)



# Send alert
def send_alert(text):

    send_message(f"🚨 ALERT:\n{text}")



# Send menu with buttons
def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            ["STATUS", "MODE"],
            ["START LIVE", "STOP LIVE"],
            ["POSITIONS", "PERFORMANCE"]
        ],
        "resize_keyboard": True
    }

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "Quant Ecosystem Command Center",
        "reply_markup": keyboard
    }

    try:

        requests.post(url, json=payload, timeout=10)

        print("Telegram menu sent")

    except Exception as e:

        print("Telegram menu error:", e)



# Receive updates
def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    try:

        response = requests.get(url, params=params, timeout=10)

        return response.json()

    except Exception as e:

        print("Telegram update error:", e)

        return None
