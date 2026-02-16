import json
import numpy as np


class PortfolioOptimizer:

    def __init__(self, broker):

        self.broker = broker


    def optimize(self):

        perf = self._load_performance()

        if not perf:
            return {}

        returns = []
        strategies = []

        for strat, data in perf.items():

            pnl = data.get("pnl", 0)
            trades = max(data.get("trades", 1), 1)

            avg_return = pnl / trades

            returns.append(avg_return)
            strategies.append(strat)

        returns = np.array(returns)

        kelly_weights = self._kelly(returns)

        risk_parity_weights = self._risk_parity(returns)

        final_weights = (kelly_weights + risk_parity_weights) / 2

        capital = self.broker.get_balance()

        allocation = {}

        for i, strat in enumerate(strategies):

            allocation[strat] = capital * final_weights[i]

        return allocation


    def _kelly(self, returns):

        mean = np.mean(returns)

        var = np.var(returns)

        if var == 0:
            return np.ones(len(returns)) / len(returns)

        weights = returns / var

        weights = np.maximum(weights, 0)

        return weights / weights.sum()


    def _risk_parity(self, returns):

        vol = np.std(returns)

        if vol == 0:
            return np.ones(len(returns)) / len(returns)

        weights = 1 / (np.abs(returns) + 1e-6)

        return weights / weights.sum()


    def _load_performance(self):

        try:
            return json.load(open("data/strategy_performance.json"))
        except:
            return {}
