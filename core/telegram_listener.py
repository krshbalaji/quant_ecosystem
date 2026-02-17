# core/telegram_listener.py

import time
from infra.telegram_service import get_updates, send_menu
from core.mobile_command import execute_command


def listen():

    print("Telegram listener active")

    last_update_id = None

    send_menu()

    while True:

        try:

            data = get_updates(last_update_id)

            if not data["ok"]:
                time.sleep(3)
                continue

            for update in data["result"]:

                last_update_id = update["update_id"] + 1

                if "message" not in update:
                    continue

                msg = update["message"]["text"]

                print("Telegram command:", msg)

                execute_command(msg)

        except Exception as e:

            print("Telegram listener error:", e)

        time.sleep(2)
