import json
import random
from datetime import datetime

class MetaIntelligenceCore:

    def __init__(self):

        self.state_file = "data/meta_intelligence_state.json"

        self.state = {
            "mode": "INSTITUTIONAL",
            "confidence": 0.5,
            "regime_prediction": "UNKNOWN",
            "last_update": str(datetime.now())
        }

        self.load()

        print("Institutional Meta-Intelligence Core Active")

    def load(self):

        try:
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        except:
            pass

    def save(self):

        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=4)

    def predict_regime(self):

        regimes = [
            "TRENDING",
            "SIDEWAYS",
            "VOLATILE",
            "LOW_VOL"
        ]

        prediction = random.choice(regimes)

        self.state["regime_prediction"] = prediction
        self.state["confidence"] = random.uniform(0.6, 0.9)
        self.state["last_update"] = str(datetime.now())

        self.save()

        return prediction

    def should_trade_live(self):

        confidence = self.state["confidence"]

        return confidence > 0.65

meta_intelligence = MetaIntelligenceCore()
