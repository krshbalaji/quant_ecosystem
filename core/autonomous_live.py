import json
from datetime import datetime, timedelta


def allow():

    config = json.load(open("config/system_mode.json"))

    start = datetime.fromisoformat(config["start_date"])

    weeks = config["moratorium_weeks"]

    if datetime.now() > start + timedelta(weeks=weeks):

        perf = json.load(open("data/strategy_performance.json"))

        best = max(perf.values(), key=lambda x: x["pnl"])

        if best["pnl"] > 0:

            return True

    return False
