import time
from infra.telegram_service import get_updates, send_message, send_menu
from core.mobile_command import execute_command

LAST_UPDATE_ID = None


def listen():
    global LAST_UPDATE_ID

    print("Telegram listener active")

    send_menu()

    while True:

        data = get_updates(LAST_UPDATE_ID)

        if data and data.get("ok"):

            for update in data["result"]:

                LAST_UPDATE_ID = update["update_id"] + 1

                if "message" in update:

                    text = update["message"].get("text", "")

                    if text:

                        print("Telegram command:", text)

                        response = execute_command(text)

                        if response:
                            send_message(response)

        time.sleep(1)
