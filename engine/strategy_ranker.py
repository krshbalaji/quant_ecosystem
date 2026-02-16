class StrategyRanker:

    def rank(self, strategies):

        ranked = sorted(
            strategies,
            key=lambda s: (s["sharpe"] * 0.4 +
                           s["return"] * 0.4 -
                           abs(s["drawdown"]) * 0.2),
            reverse=True
        )

        return ranked
