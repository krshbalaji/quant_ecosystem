import time
from infra.telegram_service import get_updates, send_menu, send_alert
from core.mobile_command import execute_command

LAST_UPDATE_ID = None


def listen():
    global LAST_UPDATE_ID

    print("Telegram listener active")

    while True:
        try:
            updates = get_updates(LAST_UPDATE_ID)

            if not updates or "result" not in updates:
                time.sleep(2)
                continue

            for update in updates["result"]:

                LAST_UPDATE_ID = update["update_id"] + 1

                if "message" not in update:
                    continue

                message = update["message"]

                if "text" not in message:
                    continue

                text = message["text"]
                chat_id = message["chat"]["id"]

                print(f"Telegram command received: {text}")

                if text == "/start":
                    send_menu()
                    continue

                execute_command(text)

        except Exception as e:
            print("Telegram listener error:", e)

        time.sleep(2)
