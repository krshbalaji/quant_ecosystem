class BacktestLab:

    def run(self, strategy, df):

        pnl = 0
        trades = 0

        for signal in strategy.generate(df):

            pnl += signal["pnl"]
            trades += 1

        sharpe = pnl / max(1, trades)

        return {
            "pnl": pnl,
            "trades": trades,
            "sharpe": sharpe
        }
