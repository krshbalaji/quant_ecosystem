# infra/telegram_service.py

import requests
import json
import os

SECRETS_FILE = "infra/secrets.json"


def load_secrets():

    if not os.path.exists(SECRETS_FILE):
        print("Telegram secrets.json missing")
        return None, None

    with open(SECRETS_FILE, "r") as f:
        data = json.load(f)

    return data.get("TELEGRAM_TOKEN"), data.get("TELEGRAM_CHAT_ID")


TOKEN, CHAT_ID = load_secrets()


def send_message(text):

    if not TOKEN or not CHAT_ID:
        print("Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        requests.post(url, json=payload, timeout=10)
        print("Telegram message sent")

    except Exception as e:
        print("Telegram send error:", e)


def send_menu():

    if not TOKEN or not CHAT_ID:
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    keyboard = {
        "keyboard": [
            ["STATUS", "START LIVE"],
            ["STOP LIVE", "FORCE PAPER"],
            ["SHUTDOWN", "RESTART"]
        ],
        "resize_keyboard": True
    }

    payload = {
        "chat_id": CHAT_ID,
        "text": "Quant Ecosystem Control Panel",
        "reply_markup": keyboard
    }

    requests.post(url, json=payload)


def send_alert(text):
    send_message("🚨 " + text)


def get_updates(offset=None):

    if not TOKEN:
        return None

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    params = {"timeout": 30}

    if offset:
        params["offset"] = offset

    try:
        r = requests.get(url, params=params, timeout=35)
        return r.json()

    except Exception as e:
        print("Telegram update error:", e)
        return None
