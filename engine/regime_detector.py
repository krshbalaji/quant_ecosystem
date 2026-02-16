import numpy as np


class RegimeDetector:

    def detect(self, prices):
        returns = np.diff(prices)

        vol = np.std(returns)
        trend = prices[-1] - prices[0]

        if vol > 2:
            return "volatile"
        elif abs(trend) > 5:
            return "trend"
        else:
            return "sideways"
