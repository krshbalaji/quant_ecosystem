import json
import os

class SafetyGuard:

    def __init__(self):

        self.file = "data/equity.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump({"peak": 8000, "current": 8000}, f)


    def update(self, equity):

        data = self._load()

        if equity > data["peak"]:
            data["peak"] = equity

        data["current"] = equity

        self._save(data)


    def allow_trading(self):

        data = self._load()

        peak = data["peak"]
        current = data["current"]

        drawdown = (peak - current) / peak

        if drawdown >= 0.05:

            print("SAFETY GUARD: Drawdown exceeded 5%")

            return False

        return True


    def _load(self):

        with open(self.file, "r") as f:
            return json.load(f)


    def _save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f)
