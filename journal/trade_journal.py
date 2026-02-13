import csv
import os
from datetime import datetime


class TradeJournal:

    FILE = "journal/trades.csv"

    def log(self, symbol, side, qty, price, pnl=0):

        exists = os.path.exists(self.FILE)

        with open(self.FILE, "a", newline="") as f:

            writer = csv.writer(f)

            if not exists:
                writer.writerow(["time","symbol","side","qty","price","pnl"])

            writer.writerow([
                datetime.now(),
                symbol,
                side,
                qty,
                price,
                pnl
            ])
