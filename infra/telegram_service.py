import os
import requests
import threading
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

last_update_id = None


def send_message(text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    try:
        requests.post(url, json=payload)
        print("Telegram message sent")
    except Exception as e:
        print("Telegram send error:", e)


def send_menu():
    keyboard = {
        "keyboard": [
            ["/status", "/equity"],
            ["/mode", "/performance"],
            ["/leaderboard", "/sparks"]
        ],
        "resize_keyboard": True
    }

    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "🏛 Institutional Control Panel",
        "reply_markup": keyboard
    }

    requests.post(url, json=payload)
    print("Telegram menu sent")


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30}
    
    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)
    return response.json()

    if data["ok"]:
        for update in data["result"]:
            last_update_id = update["update_id"] + 1
            yield update
