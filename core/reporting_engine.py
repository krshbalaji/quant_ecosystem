import json
from datetime import datetime


class ReportingEngine:

    def log_trade(self, trade):

        file = "data/trades.json"

        try:
            data = json.load(open(file))
        except:
            data = []

        trade["timestamp"] = str(datetime.now())

        data.append(trade)

        json.dump(data, open(file, "w"), indent=4)


    def generate_report(self):

        data = json.load(open("data/trades.json"))

        pnl = sum([t["pnl"] for t in data])

        print("Total PnL:", pnl)
