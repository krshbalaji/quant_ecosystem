import json
import os
import numpy as np


class RLAllocator:

    def __init__(self, broker):

        self.broker = broker

        self.file = "data/rl_memory.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            json.dump({}, open(self.file, "w"))


    def allocate(self):

        memory = self._load()

        capital = self.broker.get_balance()

        if not memory:

            return {}

        scores = np.array([memory[s]["score"] for s in memory])

        scores = np.maximum(scores, 0.01)

        weights = scores / scores.sum()

        allocation = {}

        for i, strat in enumerate(memory):

            allocation[strat] = capital * weights[i]

        return allocation


    def update(self, strategy, reward):

        memory = self._load()

        if strategy not in memory:

            memory[strategy] = {

                "score": 1.0,
                "visits": 0
            }

        memory[strategy]["score"] += reward * 0.1

        memory[strategy]["visits"] += 1

        self._save(memory)


    def _load(self):

        return json.load(open(self.file))


    def _save(self, memory):

        json.dump(memory, open(self.file, "w"), indent=4)
