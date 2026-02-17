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
