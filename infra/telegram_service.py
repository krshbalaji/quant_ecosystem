import requests
import json
from infra.secrets import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


# SEND MESSAGE
def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    requests.post(url, json=payload)


# CREATE MENU BUTTONS
def send_menu():

    url = f"{BASE_URL}/sendMessage"

    keyboard = {
        "keyboard": [
            ["STATUS", "MODE"],
            ["START LIVE", "STOP LIVE"],
            ["START PAPER", "STOP PAPER"],
            ["FORCE EVOLVE", "EMERGENCY STOP"],
            ["PORTFOLIO", "LEADERBOARD"]
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


# LISTEN FOR COMMANDS
def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    r = requests.get(url, params=params)

    return r.json()
