import json
import os


class PerformanceRegistry:

    def __init__(self):

        self.file = "data/strategy_performance.json"

        if not os.path.exists(self.file):

            json.dump({}, open(self.file, "w"))


    def update(self, strategy, pnl):

        data = json.load(open(self.file))

        if strategy not in data:

            data[strategy] = {"pnl": 0, "trades": 0}

        data[strategy]["pnl"] += pnl

        data[strategy]["trades"] += 1

        json.dump(data, open(self.file, "w"))
