import json
import requests
import os

SECRETS_FILE = os.path.join(os.path.dirname(__file__), "secrets.json")

def load_secrets():
    with open(SECRETS_FILE, "r") as f:
        return json.load(f)

SECRETS = load_secrets()

TOKEN = SECRETS["TELEGRAM_TOKEN"]
CHAT_ID = str(SECRETS["TELEGRAM_CHAT_ID"])

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"


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


def send_menu():
    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            ["/status", "/dashboard"],
            ["/paper", "/live"],
            ["/leaderboard", "/sparks"],
            ["/stop"]
        ],
        "resize_keyboard": True
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


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"

    params = {"timeout": 10}

    if offset:
        params["offset"] = offset

    try:
        response = requests.get(url, params=params, timeout=15)
        return response.json()
    except:
        return None
