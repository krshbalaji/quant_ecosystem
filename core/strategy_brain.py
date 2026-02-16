class StrategyBrain:
    def __init__(self):
        self.strategy_scores = {}
        self.strategy_weights = {}

        print("Strategy Brain Activated")

    def register_strategy(self, strategy_name):
        if strategy_name not in self.strategy_scores:
            self.strategy_scores[strategy_name] = {
                "wins": 0,
                "losses": 0,
                "profit": 0,
                "trades": 0
            }
            self.strategy_weights[strategy_name] = 1.0

    def record_trade_result(self, strategy, profit):
        self.register_strategy(strategy)

        data = self.strategy_scores[strategy]
        data["trades"] += 1
        data["profit"] += profit

        if profit > 0:
            data["wins"] += 1
        else:
            data["losses"] += 1

        self.update_weight(strategy)

    def update_weight(self, strategy):
        data = self.strategy_scores[strategy]

        if data["trades"] == 0:
            return

        win_rate = data["wins"] / data["trades"]
        profit_factor = max(data["profit"], 0) + 1

        weight = win_rate * profit_factor

        self.strategy_weights[strategy] = weight

    def get_weight(self, strategy):
        return self.strategy_weights.get(strategy, 1.0)

    def get_best_strategy(self):
        if not self.strategy_weights:
            return None

        return max(self.strategy_weights, key=self.strategy_weights.get)
