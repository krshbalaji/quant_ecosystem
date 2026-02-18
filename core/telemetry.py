import json
import os
import datetime

DATA_FILE = "data/telemetry.json"

def update_telemetry(strategy_name=None, equity=None, strategy_scores=None):

    os.makedirs("data", exist_ok=True)

    data = {}

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    if strategy_name:
        data["last_strategy"] = strategy_name

    if equity:
        data.setdefault("equity_curve", []).append({
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "value": equity
        })

    if strategy_scores:
        data["strategy_scores"] = strategy_scores

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
