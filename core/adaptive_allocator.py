import json
import os


class AdaptiveAllocator:

    def __init__(self, broker):

        self.broker = broker

        self.file = "data/allocation_state.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            json.dump({}, open(self.file, "w"))


    def allocate(self, strategy):

        capital = self.broker.get_balance()

        perf = self._load_performance()

        score = perf.get(strategy, {}).get("pnl", 0)

        weight = self._compute_weight(score)

        allocation = capital * weight

        print(f"Allocator: {strategy} weight={weight:.2f} allocation={allocation:.2f}")

        return allocation


    def _compute_weight(self, score):

        if score <= 0:

            return 0.01   # 1%

        elif score < 1000:

            return 0.02   # 2%

        elif score < 5000:

            return 0.05   # 5%

        elif score < 20000:

            return 0.10   # 10%

        else:

            return 0.20   # 20%


    def _load_performance(self):

        try:
            return json.load(open("data/strategy_performance.json"))
        except:
            return {}
