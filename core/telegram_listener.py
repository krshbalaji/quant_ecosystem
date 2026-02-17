import time
from infra.telegram_service import get_updates, send_menu


def listen():

    print("Telegram listener started")

    send_menu()

    offset = None

    while True:

        try:

            data = get_updates(offset)

            if not data.get("ok"):
                time.sleep(2)
                continue

            for update in data.get("result", []):

                offset = update["update_id"] + 1

                if "message" not in update:
                    continue

                msg = update["message"]

                text = msg.get("text", "")

                print("Telegram command:", text)

        except Exception as e:

            print("Telegram listener error:", e)

        time.sleep(2)
