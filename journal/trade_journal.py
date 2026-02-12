import csv
import os
import datetime


class TradeJournal:

    FILE = "journal/trades.csv"

    def log(self, symbol, side, qty, price, capital):

        new = not os.path.exists(self.FILE)

        with open(self.FILE, "a", newline="") as f:

            w = csv.writer(f)

            if new:
                w.writerow(["time","symbol","side","qty","price","capital"])

            w.writerow([
                datetime.datetime.now(),
                symbol,
                side,
                qty,
                price,
                capital
            ])
