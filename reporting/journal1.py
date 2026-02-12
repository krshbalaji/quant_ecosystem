# ======================================================
# reporting/journal.py
# Trade Journal + Export
# ======================================================

import csv
import datetime


class TradeJournal:

    def __init__(self):
        self.rows = []

    def record(self, side, qty, entry, exit, pnl):

        self.rows.append([
            datetime.datetime.now(),
            side,
            qty,
            entry,
            exit,
            pnl
        ])

    def export(self):

        filename = "reports/trades.csv"

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "Side", "Qty", "Entry", "Exit", "PnL"])
            writer.writerows(self.rows)

        print("📊 Trade report saved ->", filename)
