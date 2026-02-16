import json
from infra.telegram_service import send_message


def set_mode(mode):

    json.dump(
        {"mode": mode},
        open("config/trading_mode.json", "w")
    )

    send_message(f"Trading mode changed to {mode}")


def get_status(broker):

    balance = broker.get_balance()

    send_message(f"Balance: {balance}")
