import json


class EquityTracker:

    def __init__(self, broker):

        self.broker = broker


    def update(self):

        equity = self.broker.get_balance()

        json.dump(
            {"equity": equity},
            open("data/equity.json", "w")
        )

        return equity
