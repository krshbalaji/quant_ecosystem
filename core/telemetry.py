# core/telemetry.py

import json
import os
import datetime

DATA_FILE = "data/telemetry.json"

def _load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def _save(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def record_strategy_evolution(strategy_name):

    data = _load()

    data["last_strategy"] = strategy_name
    data.setdefault("strategy_history", []).append({
        "strategy": strategy_name,
        "time": datetime.datetime.now().isoformat()
    })

    _save(data)

def update_equity(equity_value):

    data = _load()

    data.setdefault("equity_curve", []).append({
        "time": datetime.datetime.now().isoformat(),
        "value": equity_value
    })

    _save(data)

def get_telemetry():
    return _load()


LOG_FILE = "data/strategy_logs.json"

def record_strategy_evolution(name):
    os.makedirs("data", exist_ok=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({"strategy": name})

    with open(LOG_FILE, "w") as f:
        json.dump(data, f)


def get_leaderboard():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    count = {}
    for item in data:
        s = item["strategy"]
        count[s] = count.get(s, 0) + 1

    sorted_board = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_board
