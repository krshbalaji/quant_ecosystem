import json
import os
from datetime import datetime

class PerformanceTracker:

    def __init__(self, file="data/performance.json"):
        self.file = file
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def record_trade(self, strategy, pnl):

        data = self._load()

        if strategy not in data:
            data[strategy] = {
                "trades": 0,
                "wins": 0,
                "losses": 0,
                "total_pnl": 0.0,
                "score": 0.5
            }

        s = data[strategy]

        s["trades"] += 1
        s["total_pnl"] += pnl

        if pnl > 0:
            s["wins"] += 1
        else:
            s["losses"] += 1

        winrate = s["wins"] / s["trades"]

        # adaptive score formula
        s["score"] = (winrate * 0.7) + (max(min(s["total_pnl"]/10000, 1), -1) * 0.3)

        self._save(data)

    def get_score(self, strategy):

        data = self._load()

        if strategy not in data:
            return 0.5

        return data[strategy]["score"]

    def best_strategy(self):

        data = self._load()

        if not data:
            return None

        return max(data, key=lambda x: data[x]["score"])

    def _load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def _save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
