"""
Leaderboard Engine
Ranks strategies by performance
"""

import json
import os


class Leaderboard:

    def __init__(self):

        self.file = "data/strategy_performance.json"

        os.makedirs("data", exist_ok=True)


    def update(self):

        try:

            data = self._load()

            ranked = sorted(
                data.items(),
                key=lambda x: x[1].get("pnl", 0),
                reverse=True
            )

            print("Leaderboard:")

            for name, stats in ranked[:10]:

                print(name, stats.get("pnl", 0))

        except Exception as e:

            print("Leaderboard error:", e)


    def _load(self):

        try:
            return json.load(open(self.file))
        except:
            return {}
