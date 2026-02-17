import json
import os

FILE = "data/escalation_state.json"

LEVELS = [500, 1000, 2000, 4000, 8000]

MIN_CONFIDENCE = 0.65
MAX_DRAWDOWN = 0.10


class EscalationLadder:

    def __init__(self):

        print("Escalation Ladder initialized")

        if not os.path.exists(FILE):

            self.save({"level": 0})


    def get_capital(self, broker, confidence, drawdown):

        state = self.load()

        level = state["level"]

        if confidence > MIN_CONFIDENCE and drawdown < MAX_DRAWDOWN:

            level = min(level + 1, len(LEVELS) - 1)

        else:

            level = max(level - 1, 0)

        self.save({"level": level})

        capital = min(LEVELS[level], broker.get_available_funds())

        print(f"Escalation level: {level}, capital: {capital}")

        return capital


    def save(self, data):

        with open(FILE, "w") as f:

            json.dump(data, f)


    def load(self):

        with open(FILE) as f:

            return json.load(f)
