import time
from infra.telegram_service import get_updates, send_menu
from core.mobile_command import execute_command

LAST_UPDATE_ID = None


def listen():

    global LAST_UPDATE_ID

    print("Telegram listener active")

    send_menu()

    while True:

        try:

            response = get_updates(LAST_UPDATE_ID)

            if not response.get("ok"):
                time.sleep(2)
                continue

            updates = response.get("result", [])

            for update in updates:

                LAST_UPDATE_ID = update["update_id"] + 1

                if "message" not in update:
                    continue

                message = update["message"]

                chat_id = message["chat"]["id"]

                text = message.get("text", "")

                print(f"Telegram command received: {text}")

                execute_command(text, chat_id)

        except Exception as e:

            print(f"Telegram listener error: {e}")

        time.sleep(2)
