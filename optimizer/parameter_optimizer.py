# =========================================
# AUTO PARAMETER SEARCH
# =========================================

import itertools
from backtest.backtester import Backtester
from core.logger import log


class ParameterOptimizer:

    def __init__(self, strategy_cls, symbol, data):

        self.strategy_cls = strategy_cls
        self.symbol = symbol
        self.data = data

    def run(self):

        results = []

        ema_values = [10, 20, 30]
        sl_values = [0.5, 1, 1.5]
        tp_values = [1, 2, 3]

        for ema, sl, tp in itertools.product(ema_values, sl_values, tp_values):

            params = {
                "ema": ema,
                "sl": sl,
                "tp": tp
            }

            bt = Backtester(self.strategy_cls, self.symbol, self.data, params)

            pnl = bt.run()

            log(f"Test {params} -> {pnl}")

            results.append((params, pnl))

        best = max(results, key=lambda x: x[1])

        log(f"BEST PARAMS -> {best}")

        return best[0]
