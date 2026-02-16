from core.paper_broker import PaperBroker
from core.broker_fyers import FyersBroker


class ExecutionEngine:

    def __init__(self, mode="paper", fyers_token=None):

        if mode == "live":
            self.broker = FyersBroker(fyers_token)

        else:
            self.broker = PaperBroker()

    def execute(self, decision):

        return self.broker.place_order(
            decision["symbol"],
            decision["qty"],
            decision["side"]
        )
MAX_QTY = 10
LIVE_ENABLED = False

def execute(self, decision):

    if not LIVE_ENABLED:
        print("LIVE TRADING DISABLED")
        return None

    if decision["qty"] > MAX_QTY:
        return None

    return self.broker.place_order(
        decision["symbol"],
        decision["qty"],
        decision["side"]
    )
