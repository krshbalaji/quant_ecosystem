import json
import os
from datetime import datetime


class RiskManager:

    def __init__(self, broker, max_risk_per_trade=0.02, max_exposure=0.10, max_drawdown=0.05):

        self.broker = broker

        self.max_risk_per_trade = max_risk_per_trade
        self.max_exposure = max_exposure
        self.max_drawdown = max_drawdown

        self.state_file = "data/risk_state.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.state_file):

            funds = broker.get_available_funds()

            state = {
                "peak_equity": funds,
                "current_equity": funds,
                "exposure": 0
            }

            json.dump(state, open(self.state_file, "w"))


    def calculate_qty(self, entry, stoploss):

        capital = self.broker.get_available_funds()

        risk_amount = capital * self.max_risk_per_trade

        risk_per_unit = abs(entry - stoploss)

        if risk_per_unit == 0:
            return 0

        qty = int(risk_amount / risk_per_unit)

        return max(qty, 1)


    def allow_trade(self, entry, stoploss):

        state = self._load()

        capital = self.broker.get_available_funds()

        trade_value = entry * self.calculate_qty(entry, stoploss)

        if trade_value > capital * self.max_risk_per_trade:

            print("RiskManager: Trade exceeds risk cap")

            return False


        if state["exposure"] + trade_value > capital * self.max_exposure:

            print("RiskManager: Exposure exceeds cap")

            return False


        if self._drawdown_exceeded():

            print("RiskManager: Drawdown exceeded")

            return False


        return True


    def register_trade(self, entry, qty):

        state = self._load()

        state["exposure"] += entry * qty

        json.dump(state, open(self.state_file, "w"))


    def unregister_trade(self, entry, qty):

        state = self._load()

        state["exposure"] -= entry * qty

        json.dump(state, open(self.state_file, "w"))


    def update_equity(self, equity):

        state = self._load()

        if equity > state["peak_equity"]:

            state["peak_equity"] = equity

        state["current_equity"] = equity

        json.dump(state, open(self.state_file, "w"))


    def _drawdown_exceeded(self):

        state = self._load()

        dd = (state["peak_equity"] - state["current_equity"]) / state["peak_equity"]

        return dd >= self.max_drawdown


    def _load(self):

        return json.load(open(self.state_file))
