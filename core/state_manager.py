import json
import os
from datetime import datetime

STATE_FILE = "data/system_state.json"


class StateManager:

    def __init__(self):

        print("State Manager initialized")


    def save(self, broker, meta):

        state = {

            "equity": broker.get_available_funds(),

            "mode": meta.get("mode", "PAPER"),

            "timestamp": str(datetime.now())
        }

        with open(STATE_FILE, "w") as f:

            json.dump(state, f)


    def load(self):

        if not os.path.exists(STATE_FILE):
            return None

        with open(STATE_FILE) as f:

            return json.load(f)
