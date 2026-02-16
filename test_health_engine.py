import numpy as np

class HealthEngine:
    def __init__(self, portfolio=None):
        self.portfolio = portfolio
        self.health_score = 0
        self.ml_confidence = 0

    def evaluate(self):
        if not self.portfolio:
            return 0

        sharpe = getattr(self.portfolio, "sharpe", 0)
        drawdown = abs(getattr(self.portfolio, "drawdown", 0))

        score = 0.5

        if sharpe > 1:
            score += 0.25
        if drawdown < 0.1:
            score += 0.25

        self.health_score = round(score, 2)
        self.ml_confidence = round(self.health_score * 100, 2)

        return self.health_score

    def allocate_capital(self, total_capital):
        self.evaluate()
        return total_capital * self.health_score
