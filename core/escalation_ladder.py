import json
import os

STATE_FILE = "data/escalation_state.json"

LEVELS = [500, 1000, 2000, 4000, 8000]

MIN_CONFIDENCE = 0.65
MAX_DRAWDOWN = 0.10


class EscalationLadder:

    def __init__(self):

        print("Escalation Ladder initialized")

        if not os.path.exists(STATE_FILE):

            self.save({"level": 0})


    def get_capital(self, broker, confidence, drawdown):

        state = self.load()

        level = state.get("level", 0)

        if confidence > MIN_CONFIDENCE and drawdown < MAX_DRAWDOWN:

            level = min(level + 1, len(LEVELS) - 1)

        else:

            level = max(level - 1, 0)

        self.save({"level": level})

        capital = min(LEVELS[level], broker.get_available_funds())

        print(f"Escalation level: {level}, capital allocated: {capital}")

        return capital


    def save(self, state):

        with open(STATE_FILE, "w") as f:

            json.dump(state, f)


    def load(self):

        if not os.path.exists(STATE_FILE):

            return {"level": 0}

        with open(STATE_FILE) as f:

            return json.load(f)
