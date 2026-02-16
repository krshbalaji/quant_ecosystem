import numpy as np
import json
import os


class LSTMPredictor:

    def __init__(self):

        self.file = "data/lstm_memory.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            json.dump({"weights": [0.5, 0.5, 0.5]}, open(self.file, "w"))


    def predict(self, prices):

        if len(prices) < 3:
            return 0

        weights = self._load()

        features = np.array([
            prices[-1] - prices[-2],
            prices[-2] - prices[-3],
            np.mean(prices[-3:])
        ])

        score = np.dot(features, weights)

        if score > 0:
            return 1    # bullish

        elif score < 0:
            return -1   # bearish

        else:
            return 0    # neutral


    def train(self, prices, actual):

        weights = self._load()

        pred = self.predict(prices)

        error = actual - pred

        weights += 0.01 * error * np.array([
            prices[-1] - prices[-2],
            prices[-2] - prices[-3],
            np.mean(prices[-3:])
        ])

        self._save(weights)


    def _load(self):

        data = json.load(open(self.file))

        return np.array(data["weights"])


    def _save(self, weights):

        json.dump(
            {"weights": weights.tolist()},
            open(self.file, "w"),
            indent=4
        )
