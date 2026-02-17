# infra/telegram_service.py

import requests
import json
import os

SECRETS_FILE = "infra/secrets.json"

def load_secrets():
    if not os.path.exists(SECRETS_FILE):
        raise Exception("Telegram secrets.json missing")

    return json.load(open(SECRETS_FILE))


def send_message(text):

    secrets = load_secrets()

    token = secrets["TELEGRAM_TOKEN"]
    chat_id = secrets["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print("Telegram send_message error:", e)


def send_alert(text):

    send_message(f"🚨 {text}")


def send_menu():

    secrets = load_secrets()

    token = secrets["TELEGRAM_TOKEN"]
    chat_id = secrets["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    keyboard = {
        "keyboard": [
            ["Status", "Equity"],
            ["Enable LIVE", "Disable LIVE"],
            ["Pause", "Resume"],
            ["Shutdown"]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }

    payload = {
        "chat_id": chat_id,
        "text": "Quant Ecosystem Control Panel",
        "reply_markup": keyboard
    }

    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print("Telegram menu error:", e)


def get_updates(offset=None):

    secrets = load_secrets()

    token = secrets["TELEGRAM_TOKEN"]

    url = f"https://api.telegram.org/bot{token}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    try:
        r = requests.get(url, params=params, timeout=10)
        return r.json()
    except:
        return {}
