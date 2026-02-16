import json
import os
import numpy as np


class DRLAllocator:

    def __init__(self, broker):

        self.broker = broker

        self.weights_file = "data/drl_weights.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.weights_file):

            json.dump({}, open(self.weights_file, "w"))


    def allocate(self):

        weights = self._load()

        capital = self.broker.get_balance()

        if not weights:

            return {}

        scores = np.array(list(weights.values()))

        scores = np.exp(scores)

        probs = scores / scores.sum()

        allocation = {}

        strategies = list(weights.keys())

        for i, strat in enumerate(strategies):

            allocation[strat] = capital * probs[i]

        return allocation


    def update(self, strategy, reward):

        weights = self._load()

        if strategy not in weights:

            weights[strategy] = 0.0

        weights[strategy] += reward * 0.01

        self._save(weights)


    def _load(self):

        return json.load(open(self.weights_file))


    def _save(self, weights):

        json.dump(weights, open(self.weights_file, "w"), indent=4)
