import json
from datetime import datetime

from core.regime_detector import RegimeDetector
from core.drawdown_recovery import DrawdownRecovery


class MetaController:

    def __init__(self, broker):

        self.broker = broker

        self.regime = RegimeDetector()

        self.recovery = DrawdownRecovery(broker)

        self.file = "data/meta_state.json"


    def decide(self):

        regime = self.regime.detect()

        equity = self.broker.get_balance()

        recovery_active = self.recovery.check()

        decision = {

            "regime": regime,
            "action": "TRADE",
            "mode": "PAPER",
            "allocation_mode": "ADAPTIVE",
            "equity": equity,
            "recovery": recovery_active,
            "timestamp": str(datetime.now())

        }

        if recovery_active:

            decision["action"] = "RECOVERY"
            decision["mode"] = "PAPER"

        elif regime == "TRENDING":

            decision["action"] = "TRADE"
            decision["mode"] = "LIVE"

        elif regime == "VOLATILE":

            decision["action"] = "PAUSE"

        elif regime == "UNKNOWN":

            decision["action"] = "EVOLVE"

        json.dump(decision, open(self.file, "w"), indent=4)

        print("MetaController Decision:", decision)

        return decision
