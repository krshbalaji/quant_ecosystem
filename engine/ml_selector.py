import pandas as pd
import numpy as np


class MLSelector:
    """
    Chooses best strategy automatically using performance metrics
    """

    def __init__(self, trade_history_fetcher):
        self.fetch_history = trade_history_fetcher

    # -----------------------------------------
    # Metrics
    # -----------------------------------------
    def sharpe_ratio(self, returns):
        if len(returns) == 0:
            return 0
        return np.mean(returns) / (np.std(returns) + 1e-9)

    def win_rate(self, pnl):
        if len(pnl) == 0:
            return 0
        return (pnl > 0).mean()

    # -----------------------------------------
    # Score each strategy
    # -----------------------------------------
    def score_strategy(self, df):
        returns = df["pnl"]

        sharpe = self.sharpe_ratio(returns)
        win = self.win_rate(returns)
        trades = len(df)

        score = sharpe * 0.5 + win * 0.3 + trades * 0.2

        return {
            "score": score,
            "sharpe": sharpe,
            "win_rate": win,
            "trades": trades
        }

    # -----------------------------------------
    # Pick best
    # -----------------------------------------
    def select(self):
        history = self.fetch_history()   # from fyers_broker
        
        confidence = min(100, round(score * 100, 2))
        return best_name, best_score

        if history.empty:
            return "default"

        best_name = None
        best_score = -999

        for name, df in history.groupby("strategy"):
            m = self.score_strategy(df)

            if m["score"] > best_score:
                best_score = m["score"]
                best_name = name

        return best_name

    def retrain(self):
        df = self.fetch_history()

        df.to_csv("data/training_snapshot.csv", index=False)

        print("✅ Model refreshed using latest trades")
