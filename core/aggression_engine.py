class AggressionEngine:

    def __init__(self):
        self.mode = "CONSERVATIVE"
        self.score = 0.0

    def calculate_aggression(
        self,
        strategy_confidence,
        learning_confidence,
        capital_strength,
        heat,
        volatility
    ):

        # Heat safety (lower heat = safer)
        heat_safety = max(0, 1 - (heat / 100))

        # Market opportunity (lower volatility safer)
        opportunity = max(0, 1 - volatility)

        score = (
            strategy_confidence * 0.30 +
            learning_confidence * 0.25 +
            capital_strength * 0.20 +
            heat_safety * 0.15 +
            opportunity * 0.10
        )

        self.score = round(score, 2)

        self.mode = self._get_mode(score)

        return {
            "mode": self.mode,
            "score": self.score,
            "position_multiplier": self._position_multiplier()
        }

    def _get_mode(self, score):

        if score <= 0.30:
            return "CONSERVATIVE"

        elif score <= 0.55:
            return "BALANCED"

        elif score <= 0.75:
            return "AGGRESSIVE"

        else:
            return "ULTRA_AGGRESSIVE"

    def _position_multiplier(self):

        return {
            "CONSERVATIVE": 0.25,
            "BALANCED": 0.50,
            "AGGRESSIVE": 0.75,
            "ULTRA_AGGRESSIVE": 1.00
        }[self.mode]
