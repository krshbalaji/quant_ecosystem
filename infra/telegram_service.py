import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    raise EnvironmentError("Missing TELEGRAM_TOKEN or TELEGRAM_CHAT_ID in .env")

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


def _safe_post(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Telegram API error:", e)
        return None


def send_message(text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    return _safe_post(url, payload)


def send_menu():
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "📟 Institutional Control Panel v2",
        "reply_markup": {
            "keyboard": [
                ["/status", "/regime"],
                ["/paper", "/live"],
                ["/auto on", "/auto off"],
                ["/risk on", "/risk off"],
                ["/capital 25", "/capital 50"],
                ["/evolve"],
                ["/shutdown"]
            ],
            "resize_keyboard": True
        }
    }
    return _safe_post(url, payload)



def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 2}
    if offset is not None:
        params["offset"] = offset

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Telegram polling error:", e)
        return {}

def send_app_launcher(chat_id):
    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": "📟 Tap below to open Institutional Terminal",
        "reply_markup": {
            "keyboard": [
                [{"text": "🚀 Open Control Terminal"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
    }

    return _safe_post(url, payload)

def send_inline_menu(chat_id):
    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": "📟 Institutional Control Terminal",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "📊 System", "callback_data": "menu_system"}],
                [{"text": "⚙ Execution", "callback_data": "menu_execution"}],
                [{"text": "🧠 Strategy", "callback_data": "menu_strategy"}],
                [{"text": "🛡 Risk", "callback_data": "menu_risk"}],
                [{"text": "🚀 Autonomous", "callback_data": "menu_auto"}]
            ]
        }
    }

    return _safe_post(url, payload)

def send_launcher(chat_id):
    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": "🚀 Launch Institutional Trading Console",
        "reply_markup": {
            "keyboard": [
                [{"text": "🚀 Open Trading Console"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
    }

    return _safe_post(url, payload)

def edit_message(chat_id, message_id, text, keyboard):
    url = f"{BASE_URL}/editMessageText"

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "reply_markup": keyboard
    }

    return _safe_post(url, payload)

