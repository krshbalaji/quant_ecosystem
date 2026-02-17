# core/capital_insurance.py

import json
import os

STATE_FILE = "data/capital_insurance.json"


class CapitalInsuranceEngine:

    def __init__(self, broker):

        self.broker = broker

        self.state = self.load()

        self.update_equity()

    def load(self):

        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                return json.load(f)

        return {
            "initial_equity": None,
            "peak_equity": None,
            "insured_equity": None,
            "last_equity": None
        }

    def save(self):

        os.makedirs("data", exist_ok=True)

        with open(STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=4)

    def update_equity(self):

        equity = self.broker.get_available_funds()

        if self.state["initial_equity"] is None:

            self.state["initial_equity"] = equity
            self.state["peak_equity"] = equity
            self.state["insured_equity"] = equity * 0.90

        if equity > self.state["peak_equity"]:

            self.state["peak_equity"] = equity

            # lock 90% of peak profit
            self.state["insured_equity"] = equity * 0.90

            print("Capital Insurance: Profit locked at", self.state["insured_equity"])

        self.state["last_equity"] = equity

        self.save()

    def check_protection(self):

        equity = self.broker.get_available_funds()

        insured = self.state["insured_equity"]

        if insured is None:
            return False

        if equity < insured:

            print("Capital Insurance Triggered — trading paused")

            return True

        return False

    def allowed_capital(self):

        equity = self.broker.get_available_funds()

        insured = self.state["insured_equity"]

        if insured is None:
            return equity

        safe_capital = equity - insured

        return max(safe_capital, equity * 0.05)
