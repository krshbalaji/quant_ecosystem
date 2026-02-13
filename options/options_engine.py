import random


class OptionsEngine:
    """
    Simple backtest simulator for options strategies
    Used by optimizer
    """

    def __init__(self,
                 symbol="BANKNIFTY",
                 sl=0.20,
                 target=0.30,
                 trail=0.10,
                 strike_distance=0):

        self.symbol = symbol
        self.sl = sl
        self.target = target
        self.trail = trail
        self.strike_distance = strike_distance

    # --------------------------------
    # Dummy backtest (fast simulation)
    # --------------------------------
    def backtest(self):

        trades = random.randint(10, 40)
        wins = random.randint(5, trades)

        profit = wins * self.target * 100 - (trades - wins) * self.sl * 100
        drawdown = random.randint(50, 200)

        return {
            "profit": profit,
            "winrate": wins / trades,
            "drawdown": drawdown
        }
