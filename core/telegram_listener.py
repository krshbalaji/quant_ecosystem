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

            if not data:
                time.sleep(2)
                continue

            if not data.get("ok"):
                time.sleep(2)
                continue

            updates = data.get("result", [])

            for update in updates:

                last_update_id = update["update_id"] + 1

                message = update.get("message")

                if not message:
                    continue

                text = message.get("text")

                if not text:
                    continue

                text = text.strip().upper()

                print("Telegram command received:", text)

                execute_command(text)

        except Exception as e:

            print("Telegram listener error:", e)

        time.sleep(2)
