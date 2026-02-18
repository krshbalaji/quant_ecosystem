# core/meta_intelligence.py

import random
from core.telemetry import record_brain_state


class MetaIntelligence:

    def __init__(self):
        print("Institutional Meta-Intelligence Core Active")
        self.last_regime = "UNKNOWN"
        self.last_confidence = 0.0
        self.last_decision = "PAPER_ONLY"

    # Core evaluation engine
    def evaluate_market(self):

        regimes = ["TRENDING", "SIDEWAYS", "VOLATILE", "LOW_VOL"]

        regime = random.choice(regimes)
        confidence = round(random.uniform(0.5, 0.95), 2)

        decision = "LIVE_ALLOWED" if confidence > 0.7 else "PAPER_ONLY"

        self.last_regime = regime
        self.last_confidence = confidence
        self.last_decision = decision

        print(f"Meta Intelligence Prediction: {regime}")

        try:
            record_brain_state({
                "regime": regime,
                "confidence": confidence,
                "decision": decision
            })
        except:
            pass

        return {
            "regime": regime,
            "confidence": confidence,
            "decision": decision
        }

    # 🔁 Legacy compatibility for old launcher
    def predict_regime(self):
        return self.evaluate_market()["regime"]

    def should_trade_live(self):
        result = self.evaluate_market()
        return result["decision"] == "LIVE_ALLOWED"

    def get_confidence(self):
        return self.last_confidence


# Singleton instance
meta_intelligence = MetaIntelligence()
