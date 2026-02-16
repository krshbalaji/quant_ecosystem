import json
import os


class CompoundingEngine:

    def __init__(self, broker):

        self.broker = broker

        self.file = "data/compounding_state.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            json.dump({

                "peak": broker.get_balance(),

                "base": broker.get_balance()

            }, open(self.file, "w"))


    def capital_fraction(self):

        balance = self.broker.get_balance()

        state = self._load()

        peak = max(state["peak"], balance)

        drawdown = (peak - balance) / peak

        # fractional Kelly scaling
        if drawdown > 0.10:

            fraction = 0.01

        elif drawdown > 0.05:

            fraction = 0.02

        elif balance > peak:

            fraction = 0.05

        else:

            fraction = 0.03

        state["peak"] = peak

        self._save(state)

        print(f"Compounding fraction: {fraction}")

        return fraction


    def allocate(self, price):

        capital = self.broker.get_balance()

        fraction = self.capital_fraction()

        allocation = capital * fraction

        qty = int(allocation / price)

        return max(qty, 1)


    def _load(self):

        return json.load(open(self.file))


    def _save(self, state):

        json.dump(state, open(self.file, "w"), indent=4)
