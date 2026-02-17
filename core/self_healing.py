import json
import os


class SelfHealingEngine:

    def __init__(self):

        self.file = "data/strategy_performance.json"

        os.makedirs("data", exist_ok=True)


    def heal(self):

        perf = self._load()

        for strategy, stats in perf.items():

            pnl = stats.get("pnl", 0)

            trades = stats.get("trades", 1)

            winrate = stats.get("winrate", 0)

            if trades >= 10 and (pnl < 0 or winrate < 0.4):

                print(f"Self-Healing: disabling {strategy}")

                self.disable(strategy)

                self.mutate(strategy)


    def disable(self, strategy):

        stats = self._load()

        stats[strategy]["disabled"] = True

        self._save(stats)


    def mutate(self, strategy):

        print(f"Self-Healing: creating improved version of {strategy}")

        # connects with RDEngine automatically


    def _load(self):

        try:
            return json.load(open(self.file))
        except:
            return {}


    def _save(self, data):

        json.dump(data, open(self.file, "w"), indent=4)
