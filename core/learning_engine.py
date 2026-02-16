import json
import os
import time

class LearningEngine:

    def __init__(self, storage="brain/learning_memory.json"):
        self.storage = storage
        self.memory = self.load()

        print("Learning Engine Activated")

    def load(self):
        if os.path.exists(self.storage):
            with open(self.storage, "r") as f:
                return json.load(f)
        return {
            "trades": [],
            "performance": {
                "wins": 0,
                "losses": 0,
                "total": 0
            }
        }

    def save(self):
        os.makedirs(os.path.dirname(self.storage), exist_ok=True)
        with open(self.storage, "w") as f:
            json.dump(self.memory, f, indent=4)

    def record_trade(self, symbol, decision, outcome):
        trade = {
            "symbol": symbol,
            "decision": decision,
            "outcome": outcome,
            "timestamp": time.time()
        }

        self.memory["trades"].append(trade)

        if outcome > 0:
            self.memory["performance"]["wins"] += 1
        else:
            self.memory["performance"]["losses"] += 1

        self.memory["performance"]["total"] += 1

        self.save()

    def get_win_rate(self):
        total = self.memory["performance"]["total"]
        wins = self.memory["performance"]["wins"]

        if total == 0:
            return 0

        return wins / total
