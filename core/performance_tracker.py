# core/performance_tracker.py

import random

class PerformanceTracker:

    def __init__(self):
        self.equity = 8000
        self.pnl = 0
        self.trades = 0
        self.wins = 0

    def record_trade(self, profit):
        self.trades += 1
        self.pnl += profit
        self.equity += profit
        if profit > 0:
            self.wins += 1

    def get_stats(self):
        winrate = 0
        if self.trades > 0:
            winrate = (self.wins / self.trades) * 100

        return {
            "equity": self.equity,
            "pnl": self.pnl,
            "trades": self.trades,
            "winrate": round(winrate, 2)
        }

performance_data = {
    "equity": 8000,
    "pnl": 0,
    "trades": 0,
    "winrate": 0
}


def update_performance(equity=None, pnl=None, trades=None, winrate=None):
    if equity is not None:
        performance_data["equity"] = equity
    if pnl is not None:
        performance_data["pnl"] = pnl
    if trades is not None:
        performance_data["trades"] = trades
    if winrate is not None:
        performance_data["winrate"] = winrate


def get_performance_snapshot():
    return performance_data

# GLOBAL INSTANCE (THIS WAS MISSING)
performance_tracker = PerformanceTracker()
