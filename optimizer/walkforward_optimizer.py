import pandas as pd
import itertools
import yaml
import os
from backtest.backtester import Backtester


RESULT_PATH = "optimizer/results.csv"
BEST_PATH = "config/best_params.yaml"


class WalkForwardOptimizer:

    def __init__(self, strategies):
        self.strategies = strategies

    # --------------------------
    # Parameter grid generator
    # --------------------------
    def param_grid(self):
        return {
            "ema_fast": [10, 20, 30],
            "ema_slow": [50, 100, 200],
            "sl": [0.01, 0.015, 0.02],
            "tp": [0.02, 0.03, 0.05]
        }

    # --------------------------
    # All combinations
    # --------------------------
    def generate_combos(self):
        grid = self.param_grid()
        keys = grid.keys()
        vals = grid.values()
        return [dict(zip(keys, v)) for v in itertools.product(*vals)]

    # --------------------------
    # Optimize one strategy
    # --------------------------
    def optimize_strategy(self, strategy_cls):

        combos = self.generate_combos()
        rows = []

        for p in combos:
            bt = Backtester(strategy_cls, params=p)
            stats = bt.run()

            rows.append({
                "strategy": strategy_cls.__name__,
                **p,
                "profit": stats["profit"],
                "drawdown": stats["drawdown"],
                "winrate": stats["winrate"],
                "sharpe": stats["sharpe"]
            })

        return rows

    # --------------------------
    # Score function
    # --------------------------
    def score(self, r):
        return (
            r["profit"] * 1.0
            + r["winrate"] * 200
            + r["sharpe"] * 500
            - r["drawdown"] * 0.7
        )

    # --------------------------
    # Run optimizer
    # --------------------------
    def run(self):

        print("🚀 Running Walk-Forward Optimizer...")

        all_rows = []

        for strat in self.strategies:
            rows = self.optimize_strategy(strat)
            all_rows.extend(rows)

        df = pd.DataFrame(all_rows)

        df["score"] = df.apply(self.score, axis=1)
        df = df.sort_values("score", ascending=False)

        os.makedirs("optimizer", exist_ok=True)
        df.to_csv(RESULT_PATH, index=False)

        best = df.iloc[0].to_dict()

        best_cfg = {
            "strategy": best["strategy"],
            "params": {
                "ema_fast": int(best["ema_fast"]),
                "ema_slow": int(best["ema_slow"]),
                "sl": float(best["sl"]),
                "tp": float(best["tp"])
            }
        }

        os.makedirs("config", exist_ok=True)

        with open(BEST_PATH, "w") as f:
            yaml.dump(best_cfg, f)

        print("✅ Best strategy selected:", best_cfg)

        return best_cfg
