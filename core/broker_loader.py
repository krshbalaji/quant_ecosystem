import json

from broker.fyers_paper import PaperBroker
from core.fyers_auth import FyersBroker

from core.system_guard import SystemGuard
from core.live_control_guard import allowed as live_allowed
from core.autonomous_live import allow as autonomous_allow


def load_broker():

    guard = SystemGuard()

    try:
        config = json.load(open("config/trading_mode.json"))
        mode = config.get("mode", "PAPER").upper()
    except:
        mode = "PAPER"

    # Autonomous LIVE override after moratorium
    if autonomous_allow():

        print("MetaController: Autonomous LIVE enabled")

        try:
            return FyersBroker()
        except:
            print("LIVE broker failed → fallback PAPER")
            return PaperBroker()

    # Manual LIVE mode with safety checks
    if mode == "LIVE" and guard.allow_live() and live_allowed():

        print("LIVE mode approved")

        try:
            return FyersBroker()
        except:
            print("LIVE broker failed → fallback PAPER")
            return PaperBroker()

    # Default PAPER mode
    print("PAPER mode active")

    return PaperBroker()
