import numpy as np


class RegimeDetector:

    def detect(self, prices=None):

        if prices is None or len(prices) < 10:

            return "UNKNOWN"

        volatility = np.std(prices[-10:])

        trend = prices[-1] - prices[-10]

        if volatility > 2:

            return "VOLATILE"

        elif abs(trend) > 1:

            return "TRENDING"

        else:

            return "RANGING"
