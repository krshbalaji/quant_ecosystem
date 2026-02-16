import json
from datetime import datetime

from core.regime_detector import RegimeDetector


class MetaController:

    def __init__(self, broker):

        self.broker = broker

        self.regime = RegimeDetector()

        self.file = "data/meta_state.json"


    def decide(self):

        regime = self.regime.detect()

        equity = self.broker.get_balance()

        decision = {

            "regime": regime,
            "action": "TRADE",
            "mode": "PAPER",
            "allocation_mode": "ADAPTIVE",
            "equity": equity,
            "timestamp": str(datetime.now())

        }

        if regime == "TRENDING":

            decision["action"] = "TRADE"
            decision["mode"] = "LIVE"

        elif regime == "RANGING":

            decision["action"] = "TRADE"
            decision["mode"] = "PAPER"

        elif regime == "VOLATILE":

            decision["action"] = "PAUSE"

        elif regime == "UNKNOWN":

            decision["action"] = "EVOLVE"

        json.dump(decision, open(self.file, "w"), indent=4)

        print("MetaController Decision:", decision)

        return decision
