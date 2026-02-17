import json
import os
import sys
import subprocess

from infra.telegram_service import send_message


CONTROL_FILE = "data/system_control.json"

from core.live_control_guard import request, approve

# core/mobile_command.py

from infra.telegram_service import send_alert


from core.mode_controller import ModeController

mode_controller = ModeController()


def execute_command(command):

    command = command.lower()

    if command == "/status":
        return "System ACTIVE\nMode: " + mode_controller.get_mode()

    elif command == "/live_on":
        mode_controller.enable_live()
        return "LIVE trading ENABLED"

    elif command == "/live_off":
        mode_controller.disable_live()
        return "LIVE trading DISABLED"

    elif command == "/paper_on":
        mode_controller.enable_paper()
        return "PAPER mode ENABLED"

    elif command == "/capital":
        return "Capital protection ACTIVE"

    elif command == "/shutdown":
        return "Shutdown request received"

    else:
        return "Unknown command"


def request_live():

    request()

    send_message(
        "LIVE requested. Press APPROVE LIVE to confirm."
    )


def approve_live():

    approve()

    send_message("LIVE approved and enabled.")


def init():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CONTROL_FILE):

        json.dump({
            "trading_enabled": True,
            "mode": "PAPER"
        }, open(CONTROL_FILE, "w"))


def set_mode(mode):

    data = json.load(open(CONTROL_FILE))

    data["mode"] = mode

    json.dump(data, open(CONTROL_FILE, "w"))

    json.dump({"mode": mode}, open("config/trading_mode.json", "w"))

    send_message(f"Mode switched to {mode}")


def stop_trading():

    data = json.load(open(CONTROL_FILE))

    data["trading_enabled"] = False

    json.dump(data, open(CONTROL_FILE, "w"))

    send_message("Trading stopped")


def start_trading():

    data = json.load(open(CONTROL_FILE))

    data["trading_enabled"] = True

    json.dump(data, open(CONTROL_FILE, "w"))

    send_message("Trading started")


def restart_system():

    send_message("Restarting system")

    subprocess.Popen([sys.executable, "main.py"])

    os._exit(0)


def status(broker):

    balance = broker.get_balance()

    data = json.load(open(CONTROL_FILE))

    msg = f"""
System Status

Trading: {data['trading_enabled']}
Mode: {data['mode']}
Balance: {balance}
"""

    send_message(msg)
