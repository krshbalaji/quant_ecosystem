import json
import os
from datetime import datetime

METRICS_FILE = "data/live_metrics.json"

def update_metrics(data):
    os.makedirs("data", exist_ok=True)

    try:
        with open(METRICS_FILE, "r") as f:
            metrics = json.load(f)
    except:
        metrics = {}

    metrics.update(data)
    metrics["timestamp"] = datetime.now().isoformat()

    with open(METRICS_FILE, "w") as f:
        json.dump(metrics, f, indent=4)

def get_metrics():
    try:
        with open(METRICS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


BASE = "data/telemetry"
PERF = "data/performance"
RD = "data/rd"

os.makedirs(BASE, exist_ok=True)
os.makedirs(PERF, exist_ok=True)
os.makedirs(RD, exist_ok=True)


def write_json(path, data):
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                existing = json.load(f)
        else:
            existing = []

        existing.append(data)

        with open(path, "w") as f:
            json.dump(existing, f, indent=4)

    except:
        pass


def record_brain_state(state):

    record = {
        "timestamp": str(datetime.now()),
        "state": state
    }

    write_json(f"{BASE}/brain_state.json", record)


def record_trade(trade):

    record = {
        "timestamp": str(datetime.now()),
        "trade": trade
    }

    write_json(f"{PERF}/trade_log.json", record)


def record_strategy_evolution(strategy):

    record = {
        "timestamp": str(datetime.now()),
        "strategy": strategy
    }

    write_json(f"{RD}/evolution_history.json", record)


def record_system_health(health):

    record = {
        "timestamp": str(datetime.now()),
        "health": health
    }

    write_json(f"{BASE}/system_health.json", record)
