def best_strategy(strategies, df):

    best = None
    best_score = 0

    for s in strategies:
        score = s["backtest"](df)
        if score > best_score:
            best_score = score
            best = s

    return best
