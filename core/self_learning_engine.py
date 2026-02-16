class SelfLearningEngine:

    def __init__(self, strategy_brain):
        self.strategy_brain = strategy_brain

        print("Self Learning Engine Activated")

    def learn_from_trade(self, strategy, entry_price, exit_price, qty):

        profit = (exit_price - entry_price) * qty

        self.strategy_brain.record_trade_result(strategy, profit)

        return {
            "profit": profit,
            "strategy_weight": self.strategy_brain.get_weight(strategy)
        }
