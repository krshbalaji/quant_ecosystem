import pandas as pd


class WalkForwardEngine:

    def run(self, strategy, df, train_size=60, test_size=20):

        results = []
        start = 0

        while start + train_size + test_size <= len(df):

            train = df.iloc[start:start+train_size]
            test = df.iloc[start+train_size:start+train_size+test_size]

            strategy.optimize(train)
            performance = strategy.backtest(test)

            results.append(performance)

            start += test_size

        return pd.DataFrame(results)
