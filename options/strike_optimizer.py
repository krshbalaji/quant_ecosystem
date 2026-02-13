# ======================================
# AUTO STRIKE OPTIMIZER
# ======================================

class StrikeOptimizer:

    def choose(self, spot):

        step = 100

        atm = round(spot / step) * step

        return {
            "ATM": atm,
            "ITM": atm - step,
            "OTM": atm + step
        }
