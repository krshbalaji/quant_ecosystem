import time

from infra.telegram_service import get_updates, send_alert, send_menu

from core.mobile_command import (
    set_mode,
    stop_trading,
    start_trading,
    restart_system,
    status,
    request_live,
    approve_live
)


last_update_id = None


def listen(broker):

    global last_update_id

    print("Telegram listener started")

    send_menu()

    while True:

        try:

            updates = get_updates(last_update_id)

            for update in updates:

                last_update_id = update["update_id"] + 1

                if "message" not in update:
                    continue

                msg = update["message"].get("text", "")

                if msg == "Switch PAPER":

                    set_mode("PAPER")
                    send_alert("Switched to PAPER")

                elif msg == "Request LIVE":

                    request_live()

                elif msg == "Approve LIVE":

                    approve_live()

                elif msg == "Stop Trading":

                    stop_trading()

                elif msg == "Start Trading":

                    start_trading()

                elif msg == "Restart System":

                    restart_system()

                elif msg == "Status":

                    status(broker)

                elif msg == "Balance":

                    bal = broker.get_balance()
                    send_alert(f"Balance: {bal}")

                elif msg == "Leaderboard":

                    send_alert("Leaderboard requested")

        except Exception as e:

            print("Telegram listener error:", e)

        time.sleep(2)
