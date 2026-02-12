import random

class Optimizer:

    def __init__(self, strategy_class, backtester):
        self.strategy_class = strategy_class
        self.backtester = backtester

    def search(self):

        best_score = -999
        best_params = None

        # try 20 random combos
        for _ in range(20):

            params = {
                "period": random.randint(10, 40),
                "sl": random.uniform(0.5, 2),
                "tp": random.uniform(1, 4)
            }

            result = self.backtester.run(self.strategy_class, params)

            score = result["sharpe"]

            if score > best_score:
                best_score = score
                best_params = params

        return best_params
