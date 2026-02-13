def simple_backtest(strategy, df):

    wins = 0
    trades = 0

    for i in range(30, len(df)):
        sub = df.iloc[:i]
        s, _ = strategy.signal(sub)

        if s:
            trades += 1
            wins += 1

    return wins / trades if trades else 0
