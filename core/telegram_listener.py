import time
from infra.telegram_service import get_updates, send_message
from core.mobile_command import execute_command

LAST_UPDATE_ID = None

def listen():
    global LAST_UPDATE_ID

    print("Telegram listener active")

    while True:
        try:
            updates = get_updates(LAST_UPDATE_ID)

            if not updates:
                time.sleep(2)
                continue

            for update in updates:

                LAST_UPDATE_ID = update["update_id"] + 1

                if "message" not in update:
                    continue

                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                print(f"Telegram command received: {text}")

                if text == "/start":
                    send_message(chat_id,
                        "Institutional Guardian Mode Active\n\n"
                        "Available commands:\n"
                        "/status\n"
                        "/live_on\n"
                        "/live_off\n"
                        "/paper_on\n"
                        "/capital\n"
                        "/positions\n"
                        "/shutdown"
                    )

                elif text.startswith("/"):
                    response = execute_command(text)
                    send_message(chat_id, response)

        except Exception as e:
            print("Telegram listener error:", e)

        time.sleep(1)
