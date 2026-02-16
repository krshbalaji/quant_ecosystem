import json
from core.brokers.paper_broker import PaperBroker
from core.brokers.fyers_broker import FyersBroker


def load_broker():

    from core.system_guard import SystemGuard

    guard = SystemGuard()

    if mode == "LIVE" and guard.allow_live():

        print("LIVE mode enabled")

        return FyersBroker()

    else:

        print("PAPER mode enabled")

        return PaperBroker()
