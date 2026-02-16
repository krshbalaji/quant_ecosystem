import json

MIN_SCORE = 0.6


def allow(strategy):

    data = json.load(open("data/strategy_performance.json"))

    if strategy not in data:
        return False

    score = data[strategy]["pnl"]

    return score >= MIN_SCORE
