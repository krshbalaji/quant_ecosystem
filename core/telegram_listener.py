import time
from infra.telegram_service import get_updates, send_inline_menu
from core.command_router import handle_callback

LAST_UPDATE_ID = None


def listen():
    global LAST_UPDATE_ID

    print("📡 Telegram Inline Control Layer Active")

    while True:
        try:
            data = get_updates(LAST_UPDATE_ID)

            if not data or "result" not in data:
                time.sleep(2)
                continue

            for update in data["result"]:
                LAST_UPDATE_ID = update["update_id"] + 1

                # ---- CALLBACK BUTTONS ----
                if "callback_query" in update:
                    callback = update["callback_query"]
                    chat_id = callback["message"]["chat"]["id"]
                    data_value = callback["data"]

                    handle_callback(data_value, chat_id)
                    continue

                # ---- NORMAL MESSAGES ----
                if "message" in update:
                    message = update["message"]
                    chat_id = message["chat"]["id"]
                    text = message.get("text")
                    print("MESSAGE RECEIVED:", text)

                    if text == "/start":
                        from infra.telegram_service import send_launcher
                        send_launcher(chat_id)

                    elif text and "Open Trading Console" in text:
                        from core.command_router import open_dashboard
                        open_dashboard(chat_id)
                                                

        except Exception as e:
            print("Telegram listener error:", e)

        time.sleep(0.3)
