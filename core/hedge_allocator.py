import json
import os

class HedgeAllocator:
    def __init__(self, log_path="data/strategy_logs.json"):
        self.log_path = log_path

    def load_logs(self):
        if not os.path.exists(self.log_path):
            return {}

        with open(self.log_path, "r") as f:
            return json.load(f)

    def rank_strategies(self):
        logs = self.load_logs()
        ranking = []

        for name, data in logs.items():
            pnl = data.get("pnl", 0)
            winrate = data.get("winrate", 0)
            score = pnl * 0.6 + winrate * 0.4
            ranking.append((name, score))

        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking

    def top_strategy(self):
        ranked = self.rank_strategies()
        return ranked[0][0] if ranked else None
