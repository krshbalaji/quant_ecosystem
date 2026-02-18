# core/meta_intelligence.py

import random

class MetaIntelligence:

    def __init__(self):
        print("Institutional Meta-Intelligence Core Active")
        self.current_regime = "UNKNOWN"

    def predict_regime(self):
        regime = random.choice(["TRENDING", "SIDEWAYS", "VOLATILE", "LOW_VOL"])
        print(f"Meta Intelligence Prediction: {regime}")
        return regime
        self.current_regime = regime

    def should_trade_live(self):
        return self.predict_regime() == "TRENDING"

meta_intelligence = MetaIntelligence()
