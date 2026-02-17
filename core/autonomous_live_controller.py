import json
import os
from datetime import datetime, timedelta


PERFORMANCE_FILE = "data/performance.json"
STATE_FILE = "data/meta_state.json"


MIN_CONFIDENCE = 0.65
MIN_STRATEGIES = 3
MIN_DAYS = 7
MAX_DRAWDOWN = 0.10


class AutonomousLiveController:

    def __init__(self):

        print("Autonomous LIVE controller initialized")


    def evaluate(self, broker):

        confidence = self.get_confidence()

        drawdown = self.get_drawdown()

        strategies = self.get_strategy_count()

        learning_days = self.get_learning_days()

        print(
            f"LIVE check: confidence={confidence}, drawdown={drawdown}, strategies={strategies}, days={learning_days}"
        )

        if confidence < MIN_CONFIDENCE:
            return False

        if drawdown > MAX_DRAWDOWN:
            return False

        if strategies < MIN_STRATEGIES:
            return False

        if learning_days < MIN_DAYS:
            return False

        return True


    def get_confidence(self):

        if not os.path.exists(PERFORMANCE_FILE):
            return 0

        with open(PERFORMANCE_FILE) as f:

            data = json.load(f)

        if not data:
            return 0

        return sum(data.values()) / len(data)


    def get_drawdown(self):

        if not os.path.exists("data/risk_state.json"):
            return 0

        with open("data/risk_state.json") as f:

            data = json.load(f)

        return data.get("drawdown", 0)


    def get_strategy_count(self):

        return len([

            f for f in os.listdir("strategies")

            if f.endswith(".py")

        ])


    def get_learning_days(self):

        if not os.path.exists(STATE_FILE):
            return 0

        with open(STATE_FILE) as f:

            data = json.load(f)

        start = datetime.fromisoformat(data.get("start_date"))

        return (datetime.now() - start).days
