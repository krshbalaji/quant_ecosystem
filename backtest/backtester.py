import pandas as pd
import numpy as np


class Backtester:

    def __init__(self, strategy, data):

        self.strategy = strategy
        self.data = data

        self.equity = 100000
        self.equity_curve = []

    def run(self):

        for price in self.data:

            signal = self.strategy.get_signal()

            if signal:
                pnl = np.random.randn() * 50  # replace with real logic
                self.equity += pnl

            self.equity_curve.append(self.equity)

        return self.results()

    def results(self):

        eq = pd.Series(self.equity_curve)

        returns = eq.pct_change().fillna(0)

        sharpe = returns.mean() / returns.std() * np.sqrt(252)

        return {
            "final_equity": eq.iloc[-1],
            "sharpe": sharpe,
            "max_drawdown": (eq / eq.cummax() - 1).min()
        }
