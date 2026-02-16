import requests
from infra.secrets import get_telegram_token, get_telegram_chat_id


TOKEN = get_telegram_token()
CHAT_ID = get_telegram_chat_id()

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"


# Unified send function
def send_message(message):

    if not TOKEN or not CHAT_ID:

        print("Telegram credentials missing")

        return False

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    r = requests.post(url, json=payload)

    return r.json()


# Backward compatibility
def send_alert(message):

    return send_message(message)


# Menu buttons
def send_menu():

    keyboard = {
        "keyboard": [
            ["Status", "Balance"],
            ["Switch PAPER", "Request LIVE"],
            ["Approve LIVE", "Stop Trading"],
            ["Restart System", "Leaderboard"]
        ],
        "resize_keyboard": True
    }

    payload = {
        "chat_id": CHAT_ID,
        "text": "Quant Ecosystem Control Panel",
        "reply_markup": keyboard
    }

    requests.post(f"{BASE_URL}/sendMessage", json=payload)


# Get updates
def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    r = requests.get(url, params=params)

    return r.json().get("result", [])
