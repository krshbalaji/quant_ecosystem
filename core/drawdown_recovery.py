import json
import os


class DrawdownRecovery:

    def __init__(self, broker):

        self.broker = broker

        self.file = "data/drawdown_state.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            json.dump({

                "peak": broker.get_balance(),

                "recovery_mode": False

            }, open(self.file, "w"))


    def check(self):

        state = self._load()

        balance = self.broker.get_balance()

        peak = max(state["peak"], balance)

        drawdown = (peak - balance) / peak

        if drawdown >= 0.10:

            state["recovery_mode"] = True

            print("RECOVERY MODE ACTIVATED")

        elif drawdown <= 0.03:

            state["recovery_mode"] = False

            print("RECOVERY MODE DEACTIVATED")

        state["peak"] = peak

        self._save(state)

        return state["recovery_mode"]


    def position_size(self, price):

        recovery = self.check()

        capital = self.broker.get_balance()

        if recovery:

            fraction = 0.005   # 0.5% risk

        else:

            fraction = 0.03    # 3% normal risk

        allocation = capital * fraction

        qty = int(allocation / price)

        return max(qty, 1)


    def _load(self):

        return json.load(open(self.file))


    def _save(self, state):

        json.dump(state, open(self.file, "w"), indent=4)
