import json
import os

FILE = "data/strategy_metrics.json"

def record_strategy(name, pnl, win, loss):
    os.makedirs("data", exist_ok=True)

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    if name not in data:
        data[name] = {
            "trades": 0,
            "wins": 0,
            "loss": 0,
            "pnl": 0
        }

    data[name]["trades"] += 1
    data[name]["wins"] += win
    data[name]["loss"] += loss
    data[name]["pnl"] += pnl

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_all():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}
