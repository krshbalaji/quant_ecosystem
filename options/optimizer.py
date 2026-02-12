# =========================================
# Simple Strategy Optimizer
# =========================================

import numpy as np


class Optimizer:

    @staticmethod
    def best_rr(results):

        best = max(results, key=lambda x: x["pnl"])
        return best
