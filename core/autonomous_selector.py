class AutonomousSelector:
    def __init__(self):
        self.mode = "BALANCED"
        print("Autonomous Strategy Selector Activated")

    def select_mode(
        self,
        volatility: float,
        heat: float,
        capital_utilization: float,
        confidence: float
    ):

        # Defensive mode
        if heat > 70 or capital_utilization > 0.9:
            self.mode = "DEFENSIVE"

        # Conservative mode
        elif volatility > 0.6 and confidence < 0.5:
            self.mode = "CONSERVATIVE"

        # Aggressive mode
        elif volatility < 0.3 and confidence > 0.7 and heat < 40:
            self.mode = "AGGRESSIVE"

        # Balanced default
        else:
            self.mode = "BALANCED"

        return self.mode


    def get_risk_multiplier(self):

        multipliers = {
            "DEFENSIVE": 0.25,
            "CONSERVATIVE": 0.5,
            "BALANCED": 1.0,
            "AGGRESSIVE": 1.5
        }

        return multipliers.get(self.mode, 1.0)
