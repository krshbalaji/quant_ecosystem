import json


def retire_underperformers():

    data = json.load(open("data/strategy_performance.json"))

    for strat in data:

        if data[strat]["pnl"] < -1000:

            print(f"Retiring {strat}")
