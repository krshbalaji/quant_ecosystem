import json
import os
import math

PERFORMANCE_FILE = "data/performance.json"
RISK_STATE_FILE = "data/risk_state.json"


MAX_RISK = 0.25
MIN_RISK = 0.01


class GrowthOptimizer:

    def __init__(self):

        print("Growth Optimizer initialized")


    def optimize(self, capital):

        scores = self.load_scores()

        drawdown = self.get_drawdown()

        allocations = {}

        for strategy, score in scores.items():

            kelly = self.kelly_fraction(score)

            safe_kelly = self.apply_drawdown_protection(
                kelly, drawdown
            )

            allocation = capital * safe_kelly

            allocations[strategy] = allocation

        return allocations


    def kelly_fraction(self, edge):

        winrate = 0.5 + edge / 2

        payoff = 1.5

        loss = 1

        kelly = (winrate * payoff - (1 - winrate) * loss) / payoff

        return max(MIN_RISK, min(kelly, MAX_RISK))


    def apply_drawdown_protection(self, kelly, drawdown):

        if drawdown > 0.20:
            return kelly * 0.25

        if drawdown > 0.10:
            return kelly * 0.5

        return kelly


    def get_drawdown(self):

        if not os.path.exists(RISK_STATE_FILE):
            return 0

        with open(RISK_STATE_FILE) as f:
            data = json.load(f)

        return data.get("drawdown", 0)


    def load_scores(self):

        if not os.path.exists(PERFORMANCE_FILE):
            return {}

        with open(PERFORMANCE_FILE) as f:
            return json.load(f)
