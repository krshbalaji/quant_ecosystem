import requests
from infra.secrets import get_telegram_token, get_telegram_chat_id

def send_alert(message):
    token = get_telegram_token()
    chat_id = get_telegram_chat_id()

    if not token or not chat_id:
        print("❌ Telegram credentials missing")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    r = requests.post(url, json=payload)
    return r.json()
