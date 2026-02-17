# core/telegram_listener.py

import time
from infra.telegram_service import get_updates, send_message, send_menu
from core.mobile_command import execute_command


def listen():

    print("Telegram listener started")

    offset = None

    while True:

        try:

            data = get_updates(offset)

            if not data or "result" not in data:
                time.sleep(2)
                continue

            for update in data["result"]:

                offset = update["update_id"] + 1

                if "message" not in update:
                    continue

                msg = update["message"].get("text", "")
                chat_id = update["message"]["chat"]["id"]

                if msg == "/start":

                    send_menu()
                    send_message("System ready. Institutional Safety Mode active.")

                else:

                    execute_command(msg)

        except Exception as e:

            print("Telegram listener error:", e)

        time.sleep(2)
