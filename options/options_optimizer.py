import pandas as pd
import itertools
from options.options_engine import OptionsEngine


class OptionsOptimizer:

    def __init__(self, symbol="BANKNIFTY"):
        self.symbol = symbol

    # -------------------------
    # Parameter grid
    # -------------------------
    def grid(self):
        return {
            "sl_pct": [0.15, 0.20, 0.25],
            "target_pct": [0.25, 0.35, 0.50],
            "trail_pct": [0.10, 0.15],
            "strike_distance": [0, 1, 2]
        }

    # -------------------------
    def combos(self):
        g = self.grid()
        return [dict(zip(g.keys(), v)) for v in itertools.product(*g.values())]

    # -------------------------
    def run(self):

        print("🚀 Running Options Optimizer...")

        rows = []

        for p in self.combos():

            engine = OptionsEngine(
                symbol=self.symbol,
                sl=p["sl_pct"],
                target=p["target_pct"],
                trail=p["trail_pct"],
                strike_distance=p["strike_distance"]
            )

            stats = engine.backtest()

            rows.append({
                **p,
                "profit": stats["profit"],
                "winrate": stats["winrate"],
                "drawdown": stats["drawdown"]
            })

        df = pd.DataFrame(rows)
        df["score"] = df["profit"] - df["drawdown"]

        df = df.sort_values("score", ascending=False)
        df.to_csv("options/options_results.csv", index=False)

        best = df.iloc[0].to_dict()

        print("✅ Best options params:", best)

        return best
