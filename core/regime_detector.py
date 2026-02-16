import numpy as np

class RegimeDetector:

    def detect(self, prices):

        if len(prices) < 50:
            return "UNKNOWN"

        returns = np.diff(prices)

        volatility = np.std(returns)

        trend = prices[-1] - prices[0]

        if volatility > 2:
            return "VOLATILE"

        if abs(trend) > volatility * 5:
            return "TRENDING"

        return "RANGING"
