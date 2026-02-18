import time
from infra.telegram_service import get_updates, send_message, send_menu
from core.mobile_command import execute_command

LAST_UPDATE_ID = None

def listen():
    global LAST_UPDATE_ID
    print("Telegram listener active")

    while True:
        data = get_updates(LAST_UPDATE_ID)

        if "result" in data:
            for update in data["result"]:
                LAST_UPDATE_ID = update["update_id"] + 1

                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"].get("text", "")
                    execute_command(text, chat_id)
