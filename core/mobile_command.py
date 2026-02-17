import json
import os
import sys
import subprocess

from infra.telegram_service import send_message


CONTROL_FILE = "data/system_control.json"

from core.live_control_guard import request, approve

# core/mobile_command.py

from infra.telegram_service import send_alert


def execute_command(cmd):

    if cmd == "Status":

        send_alert("System running normally")

    elif cmd == "Equity":

        send_alert("Equity: ₹8000")

    elif cmd == "Enable LIVE":

        send_alert("LIVE mode request received")

    elif cmd == "Disable LIVE":

        send_alert("LIVE mode disabled")

    elif cmd == "Pause":

        send_alert("Trading paused")

    elif cmd == "Resume":

        send_alert("Trading resumed")

    elif cmd == "Shutdown":

        send_alert("System shutting down")
        exit()

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
